---
number: 1846
title: Maximum Element After Decreasing and Rearranging
difficulty: Medium
tags: [array, greedy, sorting]
date: 2026-07-29
url: https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/
---

## Approach

Naive appraoch is pretty straightforward and fast. I think it's the best approach for 99% of the cases. Easy to think. Just sort and then increment if it's possible.

Time complexity optimal solution starts with the idea that the result can be at most N which is the size of array. Then we do a counting sort to see how much we can increase at each step.

## Complexity

- Time: O(n) or O(nlogn)
- Space: O(n)
