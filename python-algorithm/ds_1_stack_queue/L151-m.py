# -*- coding: utf-8 -*-
class Solution:
    def reverseWords(self, s: str) -> str:
        stk = []
        t_str = ""
        for c in s:
            if c != " ":
                t_str += c
            else:
                # 处理连续出现多个空格的情况
                if t_str != "":
                    stk.append(t_str)
                t_str = ""
        # 最后一串容易漏掉
        if t_str != "":
            stk.append(t_str)
        res = ""
        while stk:
            sub_str = stk.pop()
            res += sub_str
            if stk:
                res += " "
        return res