"""
703. Kth Largest Element in a Stream
Difficulty: Easy
Link: https://leetcode.com/problems/kth-largest-element-in-a-stream/
"""

import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        self.minHeap = []
        for n in nums:
            heapq.heappush(self.minHeap, n)
            if len(self.minHeap) > k:
                heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
