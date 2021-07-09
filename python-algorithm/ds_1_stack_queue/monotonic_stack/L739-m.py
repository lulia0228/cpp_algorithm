# -*- coding: utf-8 -*-


# 739. 每日温度

# 单调递减栈，栈中元素永远呈单调递减排序
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0]*(len(T))
        stk = []
        for i, val in enumerate(T):
            while stk and T[stk[-1]]<val:
                idx = stk.pop()
                res[idx] = i-idx
            stk.append(i)
        return res
