# -*- coding: utf-8 -*-


# 栈类型的题目要注意判断栈是否为空
class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for c in s:
            if c in ['(', '[', '{' ]:
                stk.append(c)
            else:
                if c == ')':
                    match = '('
                elif c == ']':
                    match = '['
                elif c == '}':
                    match = '{'
                # 容易漏掉stk==[]的判断条件
                if stk == [] or stk.pop(-1) != match:
                    return False
        # 如果栈中还有值，字符串也不合法
        if stk:
            return False
        return True