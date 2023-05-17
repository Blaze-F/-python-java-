

def solution(sequence, k):
    start = 0
    end = 0
    current_sum = sequence[0]
    answer = []
    if k in sequence :
        index = sequence.index(k)
        answer = [index,index]
    else :
        for i in range(1, len(sequence)):
            current_sum += sequence[i]
            end += 1
        while current_sum > k and start <= end:
            current_sum -= sequence[start]
            start += 1
        if current_sum == k:
            answer = [start, end]
    return answer

print(solution([2, 2, 2, 2, 2], 6))