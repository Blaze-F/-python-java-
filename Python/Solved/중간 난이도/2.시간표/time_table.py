from typing import Dict, List
from string import ascii_lowercase


class MakeTimeTables:
    def make_time_table(
        self, a_time: list, b_time: list, c_time: list, d_time: list
    ) -> Dict[str, list]:
        """
        메인 함수

        Returns:
            _type_: Dict[str, list]
        """
        timetable_dict = {"a": a_time, "b": b_time, "c": c_time, "d": d_time}

        preprocessed_dict = self.preprocessor(preprocess=timetable_dict, start_time=10, end_time=18)
        
        res_list = self.calc_work_time(
            preprocessed_dict=preprocessed_dict, max_worktime_week=10, full_worktime_day=8
        )
        
        res_dict = self.convert_list_to_dict(res_list)

        return res_dict

    def preprocessor(self, preprocess: dict, start_time: int, end_time: int) -> Dict[str, list]:
        """_summary_

        Args:
            preprocess (dict): 전처리 대상 딕셔너리
            start_time (int): 영업 시작시각
            end_time (int): 영업 종료시각

        Returns:
            Dict[str, list]: key = 직원 value = 그 직원의 하루시간중 근무 가능여부
        """

        return_dict = {}
        alphabet_seq = 0
        full_working_time = end_time - start_time

        for key, value in preprocess.items():
            row = []
            for times in value:
                col = self.preprocess_time_string(
                    string=times, full_working_time=full_working_time, start_time=start_time
                )
                row.append(col)

            return_dict[f"{ascii_lowercase[alphabet_seq]}"] = row
            alphabet_seq += 1

        return return_dict

    def preprocess_time_string(self, string: str, full_working_time=8, start_time=10) -> List[bool]:
        """시간 문자열 전처리 함수

        Args:
            string (str): 시각 string
            full_working_time (int): 하루 영업시간
            start_time (int): 영업 시작시간

        Returns:
            List[bool]: 개인의 하루치 근무 가능 여부를 담은 리스트
        """

        col = [False for i in range(0, full_working_time)]

        if ";" not in string:
            work_start_block = int(string[0:2])
            work_end_block = int(string[6:8])
            # 근무 가능시간
            interval = work_end_block - work_start_block
            # 개인 시간표에 대입
            changes = [True for i in range(0, interval)]
            col[work_start_block - start_time : work_end_block - start_time] = changes

        else:
            block_list = string.split(";")
            for block in block_list:
                work_start_block = int(block[0:2])
                work_end_block = int(block[6:8])
                # 근무 가능시간
                interval = work_end_block - work_start_block
                # 개인 시간표에 대입
                changes = [True for i in range(0, interval)]
                col[work_start_block - start_time : work_end_block - start_time] = changes

        return col

    def calc_work_time(
        self,
        preprocessed_dict: dict,
        max_worktime_week=10,
        full_worktime_day=8,
        work_days_in_week=5,
    ) -> Dict[str, list]:
        """_summary_

        Args:
            preprocessed_dict (dict): 직원명을 key boolean list를 val으로 갖는 딕셔너리
            max_worktime_week (int, optional): 주간 최대 근로시간. Defaults to 10.
            full_worktime_day (int, optional): 일간 영업시간. Defaults to 8.
            work_days_in_week (int, optional): 주간 영업일. Defaults to 5.

        Returns:
            Dict[str, list]: _description_
        """

        # 직원 리스트
        workers = [key for key in preprocessed_dict]
        # 직원들 주간 근로시간
        remain_times = [0 for key in preprocessed_dict]

        # 주간 테이블 (리스트)
        time_table_week = []

        # 첫 스캔
        seq = 0
        for day in range(0, work_days_in_week):

            in_day = []
            for time_block in range(0, full_worktime_day):
                temp = []

                # 직원들 개인 시간표들에서 뽑아와 temp에 나열
                for key, value in preprocessed_dict.items():
                    temp.append(value[seq][time_block])

                worker = self.check_time_block_single(
                    workers=workers,
                    remain_times=remain_times,
                    bool_types=temp,
                    max_worktime_week=max_worktime_week,
                )

                in_day.append(worker)
                # 주간 근로시간 더하기
                if worker != "empty" and worker != "failure" and worker != "conflicted":
                    remain_times[workers.index(worker)] = remain_times[workers.index(worker)] + 1

            seq += 1
            time_table_week.append(in_day)

        # 두번째 스캔
        seq = 0
        for day in range(0, work_days_in_week):
            in_day = []
            in_day = time_table_week[day]

            for time_block in in_day:
                idx = in_day.index(time_block)
                temp = []
                # 경합시에만 발동

                if time_block == "conflicted":

                    # 직원들 개인 시간표들에서 뽑아와 temp에 나열
                    for key, value in preprocessed_dict.items():
                        temp.append(value[day][idx])

                    worker = self.check_time_block(
                        workers=workers,
                        remain_times=remain_times,
                        bool_types=temp,
                        max_worktime_week=max_worktime_week,
                    )
                    in_day[in_day.index(time_block)] = worker

                    # 주간 근로시간 더하기
                    if worker != "empty" and worker != "failure":
                        remain_times[workers.index(worker)] = (
                            remain_times[workers.index(worker)] + 1
                        )

            seq += 1
            time_table_week[day] = in_day

        return time_table_week

    def check_time_block_single(
        self, workers: list, remain_times: list, bool_types: list, max_worktime_week=10
    ) -> str:
        """
        본인만 할수있는 고유한 시간대에 투입하는 함수

        Args:
            workers (list): 직원들의 이름이 담긴 리스트입니다.
            remain_times (list): 직원들 이름순으로 주간 근로시간에 대한 정보를 담은 리스트입니다.
            bool_types (list): 직원들이 해당 시간에 일을 할수 있는지 여부를 나타낸 리스트입니다.
            max_worktime_week (int, optional): 주간 최대 근로시간입니다. Defaults to 10.

        Returns:
            str:
            단독근로 가능시 해당 직원명을 리턴
            경합시 "conflicted" 리턴
            아무도 가능하지 않은경우 empty 리턴
        """

        # 두명 이상이 가능한경우
        workable = []
        if bool_types.count(True) > 1:
            return "conflicted"
        # 1명만 가능한경우 (체크만)
        elif bool_types.count(True) == 1:
            # 주간 근로시간 체크
            if remain_times[bool_types.index(True)] >= max_worktime_week:
                return "failure"
            else:
                return workers[bool_types.index(True)]

        # 아무도 가능하지 않은경우
        else:
            return "empty"

    def check_time_block(
        self, workers: list, remain_times: list, bool_types: list, max_worktime_week=10
    ) -> str:
        """
        경합시 발동. 근로시간 소진 여부 판정.
        경합이 일어날경우 가장 적은시간동안 일한 사람 먼저 투입 (남은 근로시간이 동일할경우 정렬순으로 투입)

        Args:
            workers (list): 직원들의 이름이 담긴 리스트입니다.
            remain_times (list): 직원들 이름순으로 주간 근로시간에 대한 정보를 담은 리스트입니다.
            bool_types (list): 직원들이 해당 시간에 일을 할수 있는지 여부를 나타낸 리스트입니다.
            max_worktime_week (int, optional): 주간 최대 근로시간입니다. Defaults to 10.

        Returns:
            str:
            기본적으로 직원명을 리턴합니다.
            경합 시간대이고 가능한 사람이 있으나 시간이 전부 소진된경우 -> "failure"
        """

        empty = "empty"
        # 두명 이상이 가능한경우
        workable = []
        if bool_types.count(True) > 1:
            workable = list(filter(lambda x: bool_types[x] == True, range(len(bool_types))))
            workable_remain = []
            for worker in workable:
                workable_remain.append(remain_times[worker])
            # 주간 근로시간 체크
            if min(workable_remain) <= max_worktime_week:
                return workers[workable_remain.index(min(workable_remain))]
            else:
                return "failure"

    def convert_list_to_dict(self, full_week_list: list) -> Dict[str, list]:
        """출력 형식 변환용 간단한 함수

        Args:
            full_week_list (list):

        Returns:
            Dict[str,list]: key는 return_dict에 하드코딩
        """
        return_dict = {"월": "", "화": "", "수": "", "목": "", "금": ""}

        # 반복문
        seq = 0
        for key, value in return_dict.items():
            return_dict[key] = full_week_list[seq]
            seq += 1

        return return_dict


# Testing
import time

# 작업 코드
a_time = ["10:00~14:00", "15:00~18:00", "11:00~13:00;14:00~16:00", "10:00~11:00", "15:00~18:00"]
b_time = ["11:00~14:00", "14:00~16:00", "16:00~18:00", "10:00~11:00;12:00~13:00", "14:00~16:00"]
c_time = ["14:00~16:00", "16:00~18:00", "10:00~12:00", "12:00~14:00", "14:00~16:00"]
d_time = ["14:00~18:00", "10:00~18:00", "12:00~14:00", "14:00~15:00;16:00~17:00", "10:00~12:00"]

start = time.time()  # 시작 시간 저장

solved = MakeTimeTables()
print(solved.make_time_table(a_time=a_time, b_time=b_time, c_time=c_time, d_time=d_time))

print("time :", time.time() - start)  # 현재시각 - 시작시각 = 실행 시간

""" output
{'월': ['a', 'b', 'b', 'b', 'a', 'a', 'd', 'd'], 
'화': ['d', 'd', 'd', 'd', 'a', 'b', 'b', 'b'], 
'수': ['c', 'b', 'a', 'd', 'a', 'a', 'b', 'b'], 
'목': ['a', 'empty', 'b', 'c', 'd', 'empty', 'd', 'empty'], 
'금': ['d', 'failure', 'empty', 'empty', 'b', 'c', 'a', 'a']}
time : 0.0006315708160400391
"""
