"""
3397. Maximum Number of Distinct Elements After Operations
Difficulty: Medium
Link: https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/
"""


class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()

        lastAssigned = nums[0] - k
        unique = 1

        for i in range(1, len(nums)):
            # The ideal number is the bottom of the range, UNLESS it's already taken.
            # If it's taken, we must use lastAssigned + 1.
            candidate = max(nums[i] - k, lastAssigned + 1)

            # As long as our candidate doesn't exceed the max allowed boundary
            if candidate <= nums[i] + k:
                unique += 1
                lastAssigned = candidate

        return unique
