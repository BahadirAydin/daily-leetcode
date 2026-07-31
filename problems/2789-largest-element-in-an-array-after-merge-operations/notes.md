---
number: 2789
title: Largest Element in an Array after Merge Operations
difficulty: Medium
tags: [array, greedy]
date: 2026-07-31
url: https://leetcode.com/problems/largest-element-in-an-array-after-merge-operations/
---

## Approach

Since it asks me largest element i can possibly obtain and it says i can do an op any number of times i thought "greedy" and i was right.

going from left to right we can make left too big and sabotage ourselves

however going from right to left we will only make "right of something" greater.

snowballing. (i+1)th position always get bigger.

## Complexity

- Time: O(n)
- Space: O(1)
