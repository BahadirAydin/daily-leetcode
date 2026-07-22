"""
1. 1929. Concatenation of Array
Difficulty: Easy
Link: https://leetcode.com/problems/concatenation-of-array
"""


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)

        for i in range(len_nums):
            curr = nums[i]
            nums.append(curr)

        return nums
