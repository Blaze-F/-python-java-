class NearestChar:
    def solution(self, s: str) -> None:

        splited = s.split()

        # char : tuple
        for char in enumerate(splited):
            val = -1
            if s.count(char[0]) == 1:
                pass
            elif s.count(char[0]) > 1:
                indexes = list(filter(lambda e: splited[e] == char, range(len(splited))))

        pass


# Testing
import time


# 작업 코드

start = time.time()  # 시작 시간 저장

s = ""
solved = NearestChar()

print(solved.solution(s=s))

print("time :", time.time() - start)  # 현재시각 - 시작시각 = 실행 시간
