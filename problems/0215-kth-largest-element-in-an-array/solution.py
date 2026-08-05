"""
215. Kth Largest Element in an Array
Difficulty: Medium
Link: https://leetcode.com/problems/kth-largest-element-in-an-array/
"""

import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        minHeap = []
        for i in nums:
            heapq.heappush(minHeap, i)
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        return minHeap[0]
