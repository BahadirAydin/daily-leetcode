---
number: 49
title: Group Anagrams
difficulty: Medium
tags: [array, hash-table, sorting, string]
date: 2026-07-25
url: https://leetcode.com/problems/group-anagrams/
---

## Important Tips

- ord(char) gives its ascii value. 
- Can't use mutable key type for hash map. When using frequency arrays as keys we need to convert to an immutable tpye like a tuple

## Complexity

- Time: O(N*K)
- Space: O(N) 

N is the number of strings and K is the length of longest string.
