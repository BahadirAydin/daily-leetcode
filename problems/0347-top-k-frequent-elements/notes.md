---
number: 347
title: Top K Frequent Elements
difficulty: Medium
tags: [array, bucket-sort, counting, divide-and-conquer, hash-table, heap-priority-queue, quickselect, sorting]
date: 2026-07-27
url: https://leetcode.com/problems/top-k-frequent-elements/
---

## Approach

Bucket sort.

1. Count the frequencies.
2. Most frequent number can occur at most n time where n is the length of the array.
3. ```count[i]``` has a list consisting of all items that occur "i" times.
4. Go from right to left in count array and add it to result list. When we add k, we are done.


## Complexity

- Time: O(n)
- Space: O(n)
