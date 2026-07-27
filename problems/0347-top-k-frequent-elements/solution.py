"""
347. Top K Frequent Elements
Difficulty: Medium
Link: https://leetcode.com/problems/top-k-frequent-elements/
"""


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = [[] for _ in range(len(nums) + 1)]
        frequencies = {}

        for n in nums:
            frequencies[n] = 1 + frequencies.get(n, 0)

        for num, freq in frequencies.items():
            count[freq].append(num)

        print(count)
        res = []
        for i in range(len(count) - 1, -1, -1):
            for c in count[i]:
                res.append(c)
                if len(res) == k:
                    return res
        return res
