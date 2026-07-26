"""
75. Sort Colors
Difficulty: Medium
Link: https://leetcode.com/problems/sort-colors/
"""


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        left = 0
        right = len(nums) - 1
        current = 0

        while current <= right:
            if nums[current] == 0:
                nums[left], nums[current] = nums[current], nums[left]
                left += 1
                # Left is behind current we can increment current because we already examined everything before
                current += 1
            elif nums[current] == 1:
                current += 1
            else:
                nums[right], nums[current] = nums[current], nums[right]
                right -= 1
                # We do not increment current here because we do not know what it is. not examined.
                # and if we skip will never be examined.
                # current += 1
