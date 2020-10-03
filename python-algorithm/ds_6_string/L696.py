# -*- coding: utf-8 -*-
# @Time    : 2020/10/3 15:15
# @Author  : No Name

# 这道题不太好想到解题办法
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        preLen = 0
        curLen = 1
        count = 0
        for i in range(1, len(s)) :
            if s[i] == s[i-1] :
                curLen += 1
            else :
                preLen = curLen
                curLen = 1
            if preLen >= curLen:
                count += 1
        return count