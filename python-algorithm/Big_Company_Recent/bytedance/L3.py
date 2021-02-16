# -*- coding: utf-8 -*-

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sz = len(s)
        if sz == 0: return 0
        max_len = 1
        r_dic = {}
        for c in s :
            r_dic[c] = 0

        i, j = 0, 0
        while j < sz:
            r_dic[s[j]] += 1
            while r_dic[s[j]] > 1:
                d = s[i]
                r_dic[d] -= 1
                i += 1
            max_len = max(max_len, j-i+1)
            j += 1
        return max_len

