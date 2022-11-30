class SortDict:
    def __init__(self) -> None:
        pass

    def sort_key_downside_to_up() -> None:
        """downside_to_up"""

        d = {"dream": 0, "car": 99, "blockdmask": 1, "error": 30, "app": 20}

        # 오리지널 딕셔너리
        print(f"origin         : {d}\n")

        # dictionary.items()
        d1 = sorted(d.items())
        print(f"sorted(d.items())      : {d1}")
        print(f"dict(sorted(d.items()) : {dict(d1)}")

        print()

        # 키 값만 빼서 정렬하려는 경우, key 만 빠지기 때문에 딕셔너리가 될수 없다.
        d2 = sorted(d)
        print(f"sorted(d)       : {d2}")

    def sort_key_upside_to_down() -> None:
        d = {"dream": 0, "car": 99, "blockdmask": 1, "error": 30, "app": 20}

        # 오리지널 딕셔너리
        print(f"origin         : {d}\n")

        # dictionary.items()
        d1 = sorted(d.items(), reverse=True)
        print(f"sorted(d.items(), reverse=True)      : {d1}")
        print(f"dict(sorted(d.items(), reverse=True) : {dict(d1)}")

        print()

        # 키 값만 빼서 정렬하려는 경우
        d2 = sorted(d, reverse=True)
        print(f"sorted(d, reverse=True) : {d2}")

    def sotrt_value_upside_to() -> None:
        """람다식 사용."""
        import operator  # operator.itemgetter를 사용하기 위해 모듈 임포트

        d = {"dream": 0, "car": 99, "blockdmask": 1, "error": 30, "app": 20}

        # 오리지널 딕셔너리
        print(f"origin         : {d}\n")

        # operator.itemgetter
        d1 = sorted(d.items(), key=operator.itemgetter(1))
        print("1-1) sorted(d.items(), key=operator.itemgetter(1))의 결과")
        print(d1)

        print("\n1-2) dict(sorted(d.items(), key=operator.itemgetter(1)))의 결과")
        print(dict(d1))

        # lambda x : x[1]
        d2 = sorted(d.items(), key=lambda x: x[1])
        print("\n2-1) sorted(d.items(), key=lambda x: x[1])의 결과")
        print(d2)

        print("\n2-2) dict(sorted(d.items(), key=lambda x: x[1]))의 결과")
        print(dict(d2))

    def sort_value_downside_to() -> None:
        import operator  # operator.itemgetter를 사용하기 위해 모듈 임포트

        d = {"dream": 0, "car": 99, "blockdmask": 1, "error": 30, "app": 20}

        # 오리지널 딕셔너리
        print(f"origin         : {d}\n")

        # operator.itemgetter
        d1 = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
        print("1-1) sorted(d.items(), key=operator.itemgetter(1), reverse=True)의 결과")
        print(d1)

        print("\n1-2) dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))의 결과")
        print(dict(d1))

        # lambda x : x[1]
        d2 = sorted(d.items(), key=lambda x: x[1], reverse=True)
        print("\n2-1) sorted(d.items(), key=lambda x: x[1], reverse=True)의 결과")
        print(d2)

        print("\n2-2) dict(sorted(d.items(), key=lambda x: x[1], reverse=True))의 결과")
        print(dict(d2))
