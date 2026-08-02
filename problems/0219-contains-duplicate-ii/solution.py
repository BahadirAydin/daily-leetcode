"""
219. Contains Duplicate II
Difficulty: Easy
Link: https://leetcode.com/problems/contains-duplicate-ii/
"""


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen = {}

        for i in range(len(nums)):
            num = nums[i]
            # if the number is already in the dictionary and within k distance
            if num in seen and i - seen[num] <= k:
                return True

            # duplicates override, storing always the most recent -> shortest path
            seen[num] = i

        return False
