# -*- coding: utf-8 -*-
# @Time    : 2020/10/1 21:36
# @Author  : Heng Li
# @File    : L13.py
# @Software: PyCharm

class Solution:
    def romanToInt(self, s: str) -> int:
        record = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
        }
        res = 0
        for i in range(len(s)):
            if i < len(s)-1 and record[s[i]] < record[s[i+1]]:
                res -= record[s[i]]
            else:
                res += record[s[i]]
        return res