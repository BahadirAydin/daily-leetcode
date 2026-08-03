"""
1138. Alphabet Board Path
Difficulty: Medium
Link: https://leetcode.com/problems/alphabet-board-path/
"""


class Solution:
    def alphabetBoardPath(self, target: str) -> str:

        def findAlphabetOrder(str_):
            return ord(str_) - ord("a")

        def findCoordinate(asciiNum):
            return (asciiNum // 5, asciiNum % 5)

        currentPos = (0, 0)
        res = ""
        for c in target:
            point = findCoordinate(findAlphabetOrder(c))
            moved = (point[0] - currentPos[0], point[1] - currentPos[1])
            currentPos = point
            if moved[1] < 0:
                res += abs(moved[1]) * "L"
            if moved[0] < 0:
                res += abs(moved[0]) * "U"
            if moved[0] > 0:
                res += moved[0] * "D"
            if moved[1] > 0:
                res += moved[1] * "R"

            res += "!"
        return res
