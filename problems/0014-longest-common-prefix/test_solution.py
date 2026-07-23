from solution import Solution


def test_example_1():
    assert Solution().longestCommonPrefix(["bahadir", "aydin"]) == ""


def test_example_2():
    assert (
        Solution().longestCommonPrefix(
            ["bahadir", "bardak", "bar", "bahama"],
        )
        == "ba"
    )
