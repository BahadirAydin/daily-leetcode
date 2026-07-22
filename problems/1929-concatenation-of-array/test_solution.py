from solution import Solution


def test_example_1():
    assert Solution().getConcatenation([1, 2, 1, 3]) == [1, 2, 1, 3, 1, 2, 1, 3]


def test_empty_case():
    assert Solution().getConcatenation([]) == []
