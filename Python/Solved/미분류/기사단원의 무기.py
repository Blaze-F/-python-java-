""" 내용정리
number
limit
power
result

기본적으로 number까지의 숫자들의 약수들의 개수 구해야함.
limit 보다 넘지 않으면 그냥 약수 개수만큼만
약수 개수가 limit 보다 넘으면 그냥 power 으로 대치


제곱근을 사용하여 계산.
"""


class Knights:
    def solution(number, limit, power):
        answer = 0
        for i in range(1, number + 1):
            sqrt_i = i**0.5
            count = sum(1 for j in range(1, int(sqrt_i) + 1) if i % j == 0) * 2 - (
                0 if sqrt_i % 1 else 1
            )

            answer += power if limit < count else count

        return answer


cls = Knights()

print(cls.solution())
