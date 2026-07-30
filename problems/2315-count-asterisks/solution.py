"""
2315. Count Asterisks
Difficulty: Easy
Link: https://leetcode.com/problems/count-asterisks/
"""


class Solution:
    def countAsterisks(self, s: str) -> int:

        count = 0
        n = 0
        for c in s:
            if n % 2 == 0 and c == "*":
                count += 1
            if c == "|":
                n += 1
        return count
