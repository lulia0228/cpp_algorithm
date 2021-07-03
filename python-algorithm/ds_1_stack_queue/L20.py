# -*- coding: utf-8 -*-


# 栈类型的题目要注意判断栈是否为空
class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for c in s:
            if c not in [")", "]", "}"]:
                stk.append(c)
            else:
                # 栈内无匹配
                if stk == []: return False
                pi = stk.pop()
                if c == ")":
                    if pi != "(":
                        return False
                elif c == "]":
                    if pi != "[":
                        return False
                elif c == "}":
                    if pi != "{":
                        return False
        # 栈内有多余
        if stk != []:
            return False
        return True