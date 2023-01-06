import datetime as dt
import time
from dateutil.relativedelta import relativedelta


class Pravicies:
    def solution(self, today, terms, privacies):
        answer = []
        # datetime 객체로 전처리
        now = dt.datetime.strptime(today, "%Y.%m.%d")

        term_delta = {}
        for str in terms:
            splited = str.split(" ")
            # terms를 돌면서 딕셔너리 형태 value는 timedelta 객체로 변환
            days_peroid = relativedelta(months=int(splited[1]))
            term_delta[f"{splited[0]}"] = days_peroid

        # privaces 전처리와 판정
        for index, private in enumerate(privacies):
            splited = private.split(" ")
            private_date = dt.datetime.strptime(splited[0], "%Y.%m.%d")

            # 딕셔너리에서 추출
            months = term_delta[splited[1]]

            # 파기대상일시 리스트에 추가
            if now >= (private_date + months):
                answer.append(index + 1)

        return answer


# 작업 코드

start = time.time()  # 시작 시간 저장

solved = Pravicies()
today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
pravicies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
print(solved.solution(today=today, terms=terms, privacies=pravicies))

print("time :", time.time() - start)  # 현재시각 - 시작시각 = 실행 시간
