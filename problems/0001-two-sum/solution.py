"""
1. Two Sum
Difficulty: Easy
Link: https://leetcode.com/problems/two-sum/
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()  # key = number -> value = index

        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in hashmap:
                return [hashmap[needed], i]
            hashmap[nums[i]] = i
