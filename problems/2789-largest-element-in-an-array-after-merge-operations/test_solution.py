from .solution import Solution


def test_example_1():
    assert Solution().maxArrayValue([2, 3, 3]) == 8


def test_example_2():
    assert Solution().maxArrayValue([100, 4, 3]) == 100


def test_example_3():
    assert Solution().maxArrayValue([2, 3, 7, 9, 3]) == 21
