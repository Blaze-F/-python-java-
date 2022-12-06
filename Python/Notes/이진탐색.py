# 바이너리 서치
# data 중에서 target 을 검색하여 index 값을 return 한다.
# 없으면 None을 return한다.


def binary_search(target, data):
    data.sort()
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return mid  # 함수를 끝내버린다.
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return None


# 테스트용 코드
if __name__ == "__main__":
    li = [i**2 for i in range(11)]
    target = 9
    idx = binary_search(target, li)

    if idx:
        print(li[idx])
    else:
        print("찾으시는 타겟 {}가 없습니다".format(target))


# data는 오름차순으로 정렬된 리스트
def binary_search_recursion(target, start, end, data):
    if start > end:
        return None

    mid = (start + end) // 2

    if data[mid] == target:
        return mid
    elif data[mid] > target:
        end = mid - 1
    else:
        start = mid + 1

    return binary_search_recursion(target, start, end, data)


# 테스트용 코드
if __name__ == "__main__":
    li = [i * 3 for i in range(11)]
    target = 6
    idx = binary_search_recursion(target, 0, 10, li)

    print(li)
    print(idx)

    """
바이너리 서치 Big-0
참고자료
이진 탐색과 시간 복잡도 분석 : https://jwoop.tistory.com/9

우선, 이진 탐색을 반복할수록 남아있는 (탐색할) 자료의 개수는 1/2로 줄어든다.
1번째 실행시 탐색할 남은 자료의 개수: N
2번째 실행시 탐색할 남은 자료의 개수: N/2
3번째 실행시 탐색할 남은 자료의 개수: N/2 * 1/2
4번째 실행시 탐색할 남은 자료의 개수: N/2 * 1/2 * 1/2
K번째 실행시 탐색할 남은 자료의 개수: N*(1/2)^K
탐색이 끝나는 시점에는 남은 자료의 개수가 1이 되어야 한다. 따라서 N*(1/2)^K = 1
양 변에 2^K를 곱해주면 2^K = N > K = log2^N
K의 의미는 실행횟수 따라서 자료의 갯수 N에 따른 시행횟수는 log2^N
시간 복잡도는 BigO 표기법으로 O(logN) 으로 나타낼 수 있다.
    
    """
