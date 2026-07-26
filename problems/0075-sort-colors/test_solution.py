from .solution import Solution


def test_example_1():
    arr = [2, 0, 1, 1, 0, 2, 0]
    Solution().sortColors(arr)
    assert arr == [0, 0, 0, 1, 1, 2, 2]
