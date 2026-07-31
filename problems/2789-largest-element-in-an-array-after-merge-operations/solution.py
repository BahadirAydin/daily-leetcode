"""
2789. Largest Element in an Array after Merge Operations
Difficulty: Medium
Link: https://leetcode.com/problems/largest-element-in-an-array-after-merge-operations/
"""


class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:

        currSum = nums[-1]

        for i in range(len(nums) - 1, 0, -1):
            if currSum >= nums[i - 1]:
                currSum += nums[i - 1]
            else:
                currSum = nums[i - 1]
        return currSum
