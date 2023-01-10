import time


def solution(cap, n, deliveries, pickups):
    def get_points(array):

        points = []  # turning points
        box, index = 0, n - 1

        while index > -1:
            if array[index] == 0:
                index -= 1
                continue
            if box == 0:
                points.append(index)
            capacity = cap - box
            if array[index] <= capacity:
                box += array[index]
                index -= 1
            else:
                array[index] -= capacity
                box = 0

        return iter(points), len(points)

    (d_points, d_length), (p_points, p_length) = get_points(deliveries), get_points(pickups)

    return (
        sum(max(next(d_points, 0), next(p_points, 0)) + 1 for _ in range(max(d_length, p_length)))
        * 2
    )


"""
분석 : 
"""

# 작업 코드

start = time.time()  # 시작 시간 저장

"""
cap	n	deliveries	pickups	result
4	5	[1, 0, 3, 1, 2]	[0, 3, 0, 4, 0]	16
2	7	[1, 0, 2, 0, 1, 0, 2]	[0, 2, 0, 1, 0, 2, 0]	30
"""

cap = 4
n = 5
deliveries = [1, 0, 3, 1, 2]
pickups = [0, 3, 0, 4, 0]
print(solution(cap=cap, deliveries=deliveries, pickups=pickups, n=n))

print("time :", time.time() - start)  # 현재시각 - 시작시각 = 실행 시간
