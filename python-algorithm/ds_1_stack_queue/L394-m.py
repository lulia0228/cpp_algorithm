# -*- coding: utf-8 -*-

class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        for c in s:
            if c != "]":
                stk.append(c)
            else:
                tmp_s = ""
                while stk[-1] != "[":
                    tmp_s = stk.pop()+tmp_s
                stk.pop()
                cnt_s = ""
                # 这里需要注意栈为空的判定
                while stk and stk[-1].isdigit():
                    cnt_s = stk.pop() + cnt_s
                for _ in range(int(cnt_s)):
                    stk.append(tmp_s)
        res = ""
        while stk:
            res = stk.pop()+res
        return res
