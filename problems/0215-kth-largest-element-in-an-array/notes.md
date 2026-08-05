---
number: 215
title: Kth Largest Element in an Array
difficulty: Medium
tags: [array, divide-and-conquer, heap-priority-queue, quickselect, sorting]
date: 2026-08-05
url: https://leetcode.com/problems/kth-largest-element-in-an-array/
---

## Approach

min-heap is great for continuous data stream

## Complexity

- Time: O(Nlogk) popping and pushing is logk and we do it for n elements
- Space: O(k)
