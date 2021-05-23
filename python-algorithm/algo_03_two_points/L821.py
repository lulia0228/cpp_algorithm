# -*- coding: utf-8 -*-

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        last_lt, last_rt =  float('-inf'), float('inf')
        res= []
        for idx, x in enumerate(s):
            if x==c: last_lt = idx
            res.append(idx-last_lt)
        for i in range(len(s)-1,-1,-1):
            if s[i] == c: last_rt = i
            res[i] = min(res[i], last_rt-i)
        return res