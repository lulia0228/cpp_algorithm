# -*- coding: utf-8 -*-

# 同leetcode 3

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if  s == "": return 0
        record = {}
        for c in s:
            record[c] = 0
        i = j = 0
        max_len = 1
        while i < len(s):
            record[s[i]] += 1
            while record[s[i]] > 1:
                if s[j] in record:
                    record[s[j]] -= 1
                j += 1
            max_len = max(max_len, i-j+1)
            i += 1
        return max_len


