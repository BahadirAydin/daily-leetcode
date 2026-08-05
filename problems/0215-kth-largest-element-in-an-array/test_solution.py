from .solution import Solution


def test_example_1():
    assert Solution().findKthLargest([3, 2, 1, 5, 6, 4], 3) == 4
