# -*- coding: utf-8 -*-
# @Time    : 2020/10/1 21:21
# @Author  : Heng Li
# @File    : L387.py
# @Software: PyCharm

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d =  {}
        for c in s:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        return -1