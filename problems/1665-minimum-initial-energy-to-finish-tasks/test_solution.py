from .solution import Solution


def test_example_1():
    assert (
        Solution().minimumEffort([[1, 7], [2, 8], [3, 9], [4, 10], [5, 11], [6, 12]])
        == 27
    )


def test_example_2():
    assert Solution().minimumEffort([[1, 1], [1, 3]]) == 3
