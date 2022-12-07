import random
import sys
from typing import Dict


class RandomCombination:
    def mix_members(self, members: list, num_minimum=5, num_maximum=7) -> Dict[str, list]:
        """멤버들을 셔플한뒤 최적의 인원수를 계산하여 도출합니다.

        Args:
            members (list): _description_
            num_minimum (int, optional): Defaults to 5.
            num_maximum (int, optional): Defaults to 7.

        Returns:
            Dict[str, list]: _description_
        """
        random.shuffle(members)
        num_of_people = len(members)

        # 조 편성 계산
        data = self.calculate_peoples(
            num_minimum=num_minimum, num_maximum=num_maximum, num_of_people=num_of_people
        )

        # 팀 편성
        res = self.originate(
            members=members,
            count_of_team=data["count"],
            num_of_people=data["people_in_team"],
            lack_of_people=data["lack_of_people"],
        )
        return res

    def originate(
        self, members: list, count_of_team: int, num_of_people: int, lack_of_people: int
    ) -> Dict[str, list]:
        """팀을 구성합니다

        Returns:
            _type_: Dict[str, list]"""
        return_dict = {}

        for i in range(1, count_of_team + 1):
            # 맞아떨어질 경우
            if lack_of_people == 0:
                return_dict[f"{i}팀"] = members[0:num_of_people]
                del members[0:num_of_people]

            # 남은 인원이 있을경우
            else:
                # 마지막 팀
                if i == count_of_team:
                    return_dict[f"{i}팀"] = members
                    break

                # 인원 차출
                elif i >= (count_of_team - lack_of_people):
                    return_dict[f"{i}팀"] = members[0 : num_of_people - 1]
                    del members[0 : num_of_people - 1]

                # 모든 인원이 들어간 팀
                else:
                    return_dict[f"{i}팀"] = members[0:num_of_people]
                    del members[0:num_of_people]

        return return_dict

    def calculate_peoples(
        self, num_minimum: int, num_maximum: int, num_of_people: int
    ) -> Dict[str, int]:
        """최적의 인원수를 산출합니다.

        Returns:
            _type_: Dict[str, int]"""
        count_of_team = []
        lack_of_people = []

        num_of_people_in_team = list(range(num_minimum, num_maximum + 1))

        for i in num_of_people_in_team:
            surplus = 0
            share_i = 0
            reminder_i = 0

            share_i = num_of_people // i
            reminder_i = num_of_people % i

            # 최소 조 인원 편성까지 부족한 인원수 산출
            # 맞아떨어지면
            if reminder_i == 0:
                surplus = 0

            # 다른 조에서 분배해서 최소 인원 조를 편성해야할시
            elif reminder_i < min(num_of_people_in_team):
                surplus = min(num_of_people_in_team) - reminder_i

            # 다른 조에서 분배할 필요 없이 자체적으로 편성이 가능한경우
            else:
                surplus = 0
                reminder_i = reminder_i + 1

            # 나누어 떨어지지 않을시 여분 인원이 있을경우 각 조에서 한명씩 차출해서 채울수 있는지 판별
            if reminder_i > 0:

                # 차출 가능시 나머지 인원 + 각 팀에서 1명씩 차출하여 마지막 팀을 구성
                if min(num_of_people_in_team) < i and surplus < share_i:
                    share_i = share_i + 1

                # 차출 불가, 나머지 멤버만으로 팀 생성이 가능한경우
                elif min(num_of_people_in_team) < surplus and surplus < max(num_of_people_in_team):
                    share_i = share_i + 1

                # 차출도 불가, 팀 생성도 불가
                else:
                    share_i = sys.maxsize

            lack_of_people.append(surplus)
            count_of_team.append(share_i)

        # 기본 편성인원, 부족인원 계산
        basic_count_of_team = min(count_of_team)
        basic_num_of_people_in_team = num_of_people_in_team[count_of_team.index(min(count_of_team))]
        basic_lack_of_people = lack_of_people[count_of_team.index(min(count_of_team))]

        return_dict = {
            "count": basic_count_of_team,
            "people_in_team": basic_num_of_people_in_team,
            "lack_of_people": basic_lack_of_people,
        }

        return return_dict


# Testing
import time


# 작업 코드

start = time.time()  # 시작 시간 저장

solved = RandomCombination()
members = [i for i in range(1, 100 + 1)]
print(solved.mix_members(members=members))

print("time :", time.time() - start)  # 현재시각 - 시작시각 = 실행 시간
