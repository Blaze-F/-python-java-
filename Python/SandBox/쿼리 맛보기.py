"""문제
어떤 문제에 비슷한 형태의 질문이 여러 개 주어지는 문제를 쿼리 문제라고 부른다. 
쿼리 문제는 쿼리가 주어진 순서대로 실행해서 해결할 수도 있지만, 그것이 불가능하거나 조건이 맞는 경우에는 쿼리의 순서를 임의로 바꿔서 더 편하게 해결할 수도 있다. 
우리는 예선 문제에 쿼리에 대한 설명이 등장했기 때문에 본선 문제에 쿼리 문제가 나올 것이라는 예상을 쉽게 해볼 수 있다.

이 문제에서는 길이 n의 수열과 q개의 쿼리가 주어진다. 주어지는 쿼리의 종류는 다음과 같다.

1 a b : [a, b] 구간의 합을 구해서 출력하고, a번째 수와 b번째 수를 서로 스왑(swap) 한다.
2 a b c d : [a, b] 구간의 합에서 [c, d] 구간의 합을 뺀 값을 출력한다.
[a, b] 구간의 합이란, 수열의 a번째 부터 b번째 까지 수를 모두 더한 값을 의미한다.

입력
첫째 줄에 수열의 길이를 뜻하는 n(1 ≤ n ≤ 1,000)과 쿼리의 개수를 뜻하는 q(1 ≤ q ≤ 10,000)가 주어진다. 
둘째 줄에 길이 n의 수열이 하나의 공백을 사이에 두고 주어진다. 
수열의 각 수는 -2,147,483,648보다 크거나 같고, 2,147,483,647보다 작거나 같은 정수이다. 이후 셋째 줄 부터 q개의 줄에 걸쳐 쿼리가 주어진다. 
쿼리의 형식은 “1 a b” 또는 “2 a b c d”이다. a, b, c, d는 n보다 작거나 같은 자연수이며, a ≤ b, c ≤ d임이 보장된다.
"""
"""
5 2
3 5 -2 3 -12
2 1 3 2 4
1 2 5

0
-6

7 3
12 5 -1 0 -4 3 -10
1 2 7
2 1 4 2 3
2 1 7 3 4
-7
12
6

7 3
12 5 -1 0 -4 3 -10
1 2 7
2 1 4 2 3
2 1 7 3 4
    """

def solution() :
    ans = []
    line = input().split()
    lenght = line[0]
    qurey_count = int(line[1])
    sequence = []
    for i in input().split() :
        #str -> int
        sequence.append(int(i))
    
    
    for i in range(qurey_count) :
        query = input().split()
        if typeCheck(query[0]) :
            #구간의 합을 구해서 출력하고, a번째 수와 b번째 수를 서로 스왑(swap) 한다.
            a = int(query[1]) -1
            b = int(query[2]) 
            sum = listSum(sequence[a:b])
            #Swap
            sequence[a],sequence[b-1] = sequence[a],sequence[b-1]
            ans.append(sum)
        else :
            #[a, b] 구간의 합에서 [c, d] 구간의 합을 뺀 값을 출력한다.
            a = int(query[1]) -1
            b = int(query[2]) 
            c = int(query[3]) -1
            d = int(query[4]) 
            sum = listSum(sequence[a:b]) - listSum(sequence[c:d])
            ans.append(sum)
    
    #출력 함수
    for i in range(len(ans)) :
        print(ans[i])
    
def typeCheck(input :int) -> bool :
    #쿼리 타입 체크 함수
    if input == '1' :
        return True
    else :
        return False

def listSum(input :list) -> int :
    #리스트 구간합 구하는 함수
    summary = 0
    for i in input :
        summary += i
    return summary

# Testing
import time

# 작업 코드


start = time.time()  # 시작 시간 저장
solution()

print("time :", time.time() - start)  # 현재시각 - 시작시각 = 실행 시간

