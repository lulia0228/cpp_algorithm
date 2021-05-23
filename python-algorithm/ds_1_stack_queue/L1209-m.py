# -*- coding: utf-8 -*-

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk = []
        for i in range(len(s)):
            if i==0 or stk == [] or s[i] != stk[-1][0]:
                stk.append([s[i], 1])
            else:
                stk[-1][1] += 1
                if stk[-1][1] == k:
                    stk.pop()

        res = ""
        while stk:
            c_s = stk.pop()
            res = c_s[0]*c_s[1] + res
        return res
