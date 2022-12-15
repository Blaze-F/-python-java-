import time


class AppleCustomer:
    def solution(self, k: int, m: int, score: list) -> int:
        answer = 0
        boxes = []
        score.sort(reverse=False)

        box_count = int(len(score) // m)
        for j in range(0, box_count):
            for i in range(0, m):
                boxes.append(score.pop())
            answer += min(boxes) * m
            boxes = []

        return answer


# 작업 코드

start = time.time()  # 시작 시간 저장

solved = AppleCustomer()
m = 4
k = 3
score = [1, 2, 3, 1, 2, 3, 1]
print(solved.solution(m=m, k=k, score=score))

print("time :", time.time() - start)  # 현재시각 - 시작시각 = 실행 시간
