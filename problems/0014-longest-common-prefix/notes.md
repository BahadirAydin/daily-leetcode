---
number: 14
title: Longest Common Prefix
difficulty: Easy
tags: [array, string, trie]
date: 2026-07-23
url: https://leetcode.com/problems/longest-common-prefix
---

## Approach

Vertical scanning. Look at one column at once. If anything does not match with the first string return string up to current character.

## Complexity

- Time: O(n*m) where n is the number of strings and m is the length of shortest string
- Space: O(1)
