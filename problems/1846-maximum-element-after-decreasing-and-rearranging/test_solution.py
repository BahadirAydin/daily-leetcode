from .solution import Solution


def test_example_1():
    assert (Solution().maximumElementAfterDecrementingAndRearranging([1, 100, 61])) == 3


def test_example_2():
    assert (
        Solution().maximumElementAfterDecrementingAndRearranging([10, 1, 1, 2, 2, 2])
    ) == 3
