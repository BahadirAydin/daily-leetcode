"""
14. longest-common-prefix
Difficulty: Easy
Link: https://leetcode.com/problems/longest-common-prefix
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        for ptr in range(len(strs[0])):
            for i in range(1, len(strs)):
                if len(strs[i]) == ptr or strs[0][ptr] != strs[i][ptr]:
                    return strs[0][:ptr]
        return strs[0]
