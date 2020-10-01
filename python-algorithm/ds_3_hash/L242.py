# -*- coding: utf-8 -*-
# @Time    : 2020/10/1 20:08
# @Author  : Heng Li
# @File    : L242.py
# @Software: PyCharm

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for c in s:
            if c not in d:
                d[c]  = 1
            else:
                d[c] += 1
        for c in t:
            if c not in d:
                return False
            else:
                d[c] -= 1
        for k,v in d.items():
            if v != 0:
                return False
        return True