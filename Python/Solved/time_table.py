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
        res = self.calc_work_time(
            preprocessed_dict=preprocessed_dict, max_worktime_week=10, full_worktime_day=8
        )

        return res

    def preprocessor(self, preprocess: dict, start_time: int, end_time: int) -> Dict[str, list]:
        """
        옵션 : 전처리 함수
        시각 형태 -> 가능한 슬롯 형태로 변환 가능 10:00~11:00 -> (1,1)(True)
        bool 형태의 이차원 리스트로 변환후 딕셔너리에 넣어서 리턴 key 순서는 알파벳 순

        Returns:
            _type_: Dict[str, list]
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

    def preprocess_time_string(
        self, string: str, full_working_time: int, start_time: int
    ) -> List[bool]:

        col = [False for i in range(0, full_working_time)]

        if ";" not in string:
            work_start_block = int(string[0:2])
            work_end_block = int(string[6:8])
            interval = work_end_block - work_start_block
            changes = [True for i in range(0, interval)]
            col[work_start_block - start_time : work_end_block - start_time] = changes

        else:
            block_list = string.split(";")
            for block in block_list:
                work_start_block = int(block[0:2])
                work_end_block = int(block[6:8])
                interval = work_end_block - work_start_block
                changes = [True for i in range(0, interval)]
                col[work_start_block - start_time : work_end_block - start_time] = changes

        return col

    def calc_work_time(
        self, preprocessed_dict: dict, max_worktime_week=10, full_worktime_day=8
    ) -> Dict[str, list]:
        """


        Returns:
            _type_: Dict[str, list]
        """
        workers = [key for key in preprocessed_dict]
        remain_times = [0 for key in preprocessed_dict]
        return_dict = {"월": "", "화": "", "수": "", "목": "", "금": ""}

        for dict_key in return_dict:
            seq = 0
            in_day = []
            for time_block in range(0, full_worktime_day):
                temp = []
                for key, value in preprocessed_dict.items():
                    temp.append(value[seq][time_block])

                worker = self.check_time_block(
                    workers=workers,
                    remain_times=remain_times,
                    bool_types=temp,
                    max_worktime_week=max_worktime_week,
                )
                in_day.append(worker)
                if worker != "empty" and worker != "failure":
                    remain_times[workers.index(worker)] = remain_times[workers.index(worker)] + 1
            seq += 1
            return_dict[dict_key] = in_day

        return return_dict

    def check_time_block(
        self, workers: list, remain_times: list, bool_types: list, max_worktime_week=10
    ) -> str:
        """
        0. 아무도 일할 수 없는 시간 판정 -> "empty"
        1. 본인만 할수있는 고유한 시간대에 먼저 투입
        2. 경합이 일어날경우 가장 적은시간동안 일한 사람 먼저 투입 (남은 근로시간이 동일할경우 이름순으로 투입)
        3. 가능한 사람이 있으나 시간이 전부 소진된경우 -> "failure"
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

        # 1명만 가능한경우
        elif bool_types.count(True) == 1:
            # 주간 근로시간 체크
            if remain_times[bool_types.index(True)] > max_worktime_week:
                return "failure"
            else:
                return workers[bool_types.index(True)]

        # 아무도 가능하지 않은경우
        else:
            return "empty"


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
