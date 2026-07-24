from solution import Solution


def test_example_1():
    s = ["b", "a", "h", "a", "d", "i", "r"]
    Solution().reverseString(s)
    assert s == [
        "r",
        "i",
        "d",
        "a",
        "h",
        "a",
        "b",
    ]
