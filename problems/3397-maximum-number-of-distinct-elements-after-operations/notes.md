---
number: 3397
title: Maximum Number of Distinct Elements After Operations
difficulty: Medium
tags: [array, greedy, sorting]
date: 2026-08-01
url: https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/
---

## Approach

greedy approach again.

whenever i can change number within a range or gives me start/end intervals: SORT

sort and sweep. always choose the as small value as possible at each iteration. if "as small as possible value".

the trick is whenever we can't find unique number in a spot we SHOULD NOT end the loop right there because next numbers can be large and easily fit our uniqueness criteria.

## Complexity

- Time: O(nlogn)
- Space: O(n) or O(1) depends on sort
