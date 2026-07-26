---
number: 75
title: Sort Colors
difficulty: Medium
tags: [array, sorting, two-pointers]
date: 2026-07-26
url: https://leetcode.com/problems/sort-colors/
---

## Approach

Dutch national flag partition. 

index 0 to left -- all 0s 
nums left to current -- all 1s
nums current to right -- unexamined
nums right to n -- all 2s

## Complexity

- Time: O(n)
- Space: O(1)
