"""
1846. Maximum Element After Decreasing and Rearranging
Difficulty: Medium
Link: https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/
"""


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        return self._solve_optimal(arr)

    # 1 <= arr[i] <= 109
    # 1 <= arr.length <= 105

    def _solve_naive_sort(self, arr: List[int]) -> int:
        """Time: O(N log N), Space: O(1) or O(N) depending on sort"""
        arr.sort()

        arr[0] = 1
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                arr[i] = arr[i - 1] + 1

        return arr[-1]

    def _solve_optimal(self, arr: List[int]) -> int:
        """Time: O(N), Space: O(N) - Using Counting Sort"""

        n = len(arr)  # this is the maximum theoretical possible number
        # because we start with 1
        # and in best case we only increment by 1 until the end

        counts = [0] * n

        for num in arr:
            # any number >= 1 can just be treated as n
            counts[min(num, n) - 1] += 1

        max_value = 1
        for i in range(1, n):
            bucket_value = i + 1
            bucket_freq = counts[i]

            max_value = min(max_value + bucket_freq, bucket_value)

        return max_value
