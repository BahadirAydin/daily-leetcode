from .solution import Solution


def test_example_1():
    assert Solution().search([-1, 0, 3, 5, 9, 12], 9) == 4
