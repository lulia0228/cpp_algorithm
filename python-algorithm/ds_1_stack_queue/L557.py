# -*- coding: utf-8 -*-

class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        stk = []
        for c in s:
            if c != " ":
                stk.append(c)
            else:
                t_str = ""
                while stk:
                    t_str += stk.pop()
                res += t_str
                res += " "
        while stk:
            res += stk.pop()
        return res