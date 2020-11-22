# -*- coding: utf-8 -*-

# 同leetcode 3

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        record = {}
        for c in s:
            record[c] = 0
        i, j = 0, 0
        min_len = 1
        while j<len(s):
            record[s[j]] += 1
            while record[s[j]] > 1:
                record[s[i]] -= 1
                i += 1
            # 在循环外面判断最长值
            min_len = max(min_len, j-i+1)
            j += 1
        return min_len
