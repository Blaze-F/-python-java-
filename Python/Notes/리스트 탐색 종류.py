# 정순 탐색

py_list = [1, 2, 3, 4, 5, 5, 5, 1, 2]

"""
index()는 리스트에서 특정 원소의 인덱스를 반환해주는 함수
◼ 사용 방법은 다음 세 가지
◻ array.index(x) 리스트에서 x의 인덱스 반환
◻ array.index(x, start) 리스트[start:]에서 x의 인덱스 반환
◻ array.index(x, start, stop) 리스트[start:stop]에서 x의 인덱스 반환
    (stop은 포함되지 않음. 즉 start부터 stop-1까지의 원소들만 포함)
◼ 중복된 원소가 있으면 가장 작은 인덱스를 리턴
◼ 문자열에서도 인덱스를 찾을 수 있음
"""


class TestingListInexing:
    def reversing(self) -> None:
        for i in py_list[::-1]:
            print(i)

    def interval(self) -> None:
        for i in py_list:
            pass

    def ascending(self, start=1, end=6) -> None:
        out = []

        for i in py_list:
            pass


# Testing

solved = TestingListInexing()
print("reversing : ")
solved.reversing()
print("interval : ")
solved.interval()
