# -*- coding: utf-8 -*-


# 739. 每日温度

# 单调递减栈，栈中元素永远呈单调递减排序
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stk = []
        res = [0 for i in range(len(T))]
        for i in range(len(T)):
            while stk != [] and T[stk[-1]]<T[i]:
                # 计算出栈元素的索引和当前遍历到的元素的索引的距离
                goal_idx = stk.pop(-1)
                res[goal_idx] = i-goal_idx
            stk.append(i)
        return res