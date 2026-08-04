from .solution import Solution


def test_example_1():
    assert Solution().calPoints(["5", "2", "C", "D", "+"]) == 30
