# -*- coding: utf-8 -*-
# @Time    : 2020/10/1 21:26
# @Author  : Heng Li
# @File    : L409.py
# @Software: PyCharm

# 409. 最长回文串

# 乍一看以为要考察其它算法，用哈希就可以解决了

class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        res = 1
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        for k,v in d.items():
            if v%2 == 0:
                res += v
            else:
                res += v-1
        return len(s) if res>len(s) else res
