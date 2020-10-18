# -*- coding: utf-8 -*-


class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        sz = len(s)
        for i in range(sz-1, -1, -1):
            res += (ord(s[i])-ord('A')+1)*(26**(sz-i-1))
        return res