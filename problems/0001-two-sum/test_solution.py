from .solution import Solution


def test_example_1():
    assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]
