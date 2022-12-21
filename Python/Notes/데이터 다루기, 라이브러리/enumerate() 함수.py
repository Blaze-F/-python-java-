"""
for 루프를 돌릴때 원소와 인덱스에 동시에 접근하고싶을때 쓰는 함수. 즉 특정 문자도 쓰고싶고 그 문자의 sequence도 갖고싶을때 사용한다
"""


class ExampleOfEnumerate:
    def example(self) -> None:
        for entry in enumerate(["A", "B", "C", "네번째", "원소들"]):
            print(entry)


# testing

test = ExampleOfEnumerate()
test.example()


"""
output
(0, 'A')
(1, 'B')
(2, 'C')
(3, '네번째')
(4, '원소들')
"""
