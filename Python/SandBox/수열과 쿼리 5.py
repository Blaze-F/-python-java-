"""
문제
길이가 N인 수열 A1, A2, ..., AN이 주어진다. 이때, 다음 쿼리를 수행하는 프로그램을 작성하시오.

i j: Ai, Ai+1, ..., Aj에 존재하는 서로 다른 수의 개수를 출력한다.
입력
첫째 줄에 수열의 크기 N (1 ≤ N ≤ 100,000)이 주어진다.

둘째 줄에는 A1, A2, ..., AN이 주어진다. (1 ≤ Ai ≤ 1,000,000)

셋째 줄에는 쿼리의 개수 M (1 ≤ M ≤ 100,000)이 주어진다.

넷째 줄부터 M개의 줄에는 쿼리 i, j가 한 줄에 하나씩 주어진다. (1 ≤ i ≤ j ≤ N)

출력
각각의 쿼리마다 정답을 한 줄에 하나씩 출력한다.

(1 ≤ i ≤ j ≤ N)
"""
"""
5
1 1 2 1 3
3

1 5
2 4
3 5

3
2
3

    """

def solution() -> None :
    size = input()
    sequence = input()
    query_count = input()
    query_list = []
    
    for i in range(query_count):
        temp = []
        query_list.append(input().split())
        
    for qurey in query_list :
        
        pass
        

# Testing
import time

# 작업 코드


start = time.time()  # 시작 시간 저장

solved = None
print()

print("time :", time.time() - start)  # 현재시각 - 시작시각 = 실행 시간

