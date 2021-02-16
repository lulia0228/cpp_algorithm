# -*- coding: utf-8 -*-
# python中没有switch用法，可以用字典方式使用

class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        switch = {')': self.case1, '}': self.case2, ']': self.case3}
        for i in range(len(s)):
            if s[i] not in [')', '}', ']']:
                stk.append(s[i])
            else:
                if stk == []:  return False  # 容易漏掉
                tmp = stk.pop(-1)
                match = switch.get(s[i])()
                if match != tmp:
                    return False
        return stk == []

    def case1(self):
        return '('

    def case2(self):
        return '{'

    def case3(self):
        return '['

