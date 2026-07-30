from .solution import Solution


def test_example_1():
    assert Solution().countAsterisks("baha|d*r|*|a|yd*n") == 2


def test_example_2():
    assert Solution().countAsterisks("****") == 4


def test_example_3():
    assert Solution().countAsterisks("") == 0
