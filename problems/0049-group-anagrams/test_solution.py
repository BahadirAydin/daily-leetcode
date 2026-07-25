from .solution import Solution


def test_example_1():
    sol = Solution()
    assert sol.groupAnagrams(["bah", "ad", "ir", "hab"]) == [
        ["bah", "hab"],
        ["ad"],
        ["ir"],
    ]
