from .solution import Solution


def test_example_1():
    assert Solution().maxDistinctElements([1, 10, 2, 10, 2], 1) == 5


def test_example_2():
    assert Solution().maxDistinctElements([10, 2, 2, 2, 10, 1, 1], 1) == 6
