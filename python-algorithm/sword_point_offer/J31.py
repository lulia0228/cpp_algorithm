# -*- coding: utf-8 -*-

# 给定入栈顺序， 判断给定的序列是否是出栈序列
# 同leetcode946
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stk = []
        i = 0
        while i < len(pushed):
            while i < len(pushed) and pushed[i] != popped[0]:
                stk.append(pushed[i])
                i += 1
            popped.pop(0)
            while stk and stk[-1] == popped[0]:
                popped.pop(0)
                stk.pop(-1)
            i += 1
        return True if stk == [] else False



