# -*- coding: utf-8 -*-

# 题目：
# 给定一个乱序的栈，设计算法将其升序排列。
# ps: 允许额外使用一个栈来辅助操作

def stackSort(stk):
    tmp = [] # 单调栈
    while stk:
        peak = stk.pop()
        while tmp and tmp[-1] > peak:
            t = tmp.pop()
            stk.append(t)
        tmp.append(peak)
    return tmp