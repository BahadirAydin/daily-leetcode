---
number: 1665
title: Minimum Initial Energy to Finish Tasks
difficulty: Hard
tags: [array, greedy, sorting]
date: 2026-07-28
url: https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/
---

## Approach

(minimum - actual) is the exact energy I'm forced to have left over after finishing a task.

we always start with greater leftover values so, we have as little as possible unspent in the end.

when we do the greater (minimum-actual) tasks first, their leftovers fund the rest of the tasks.

## Complexity

- Time: O(N*logN)
- Space: O(N) -- because python sort uses Timsort, which requires O(N) worst case. in c++ it would change.. depends on sorting algorithm
