"""
49. Group Anagrams
Difficulty: Medium
Link: https://leetcode.com/problems/group-anagrams/
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            if tuple(count) in anagrams:
                anagrams[tuple(count)].append(s)
            else:
                anagrams[tuple(count)] = [s]

        return list(anagrams.values())
