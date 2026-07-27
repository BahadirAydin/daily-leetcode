from .solution import Solution


def test_example_1():
    assert Solution().topKFrequent([1, 2, 2, 3, 3, 3], 2) == [3, 2]
