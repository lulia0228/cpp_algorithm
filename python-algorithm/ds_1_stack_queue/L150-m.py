# -*- coding: utf-8 -*-
# @Time    : 2020/10/2 8:40
# @Author  : Heng Li
# @File    : L150-m.py
# @Software: PyCharm

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                stk.append(token)
            else:
                tmp_1 = int(stk.pop(-1))
                tmp_2 = int(stk.pop(-1))
                if token == '+':
                    stk.append(tmp_2 + tmp_1)
                elif token == '-':
                    stk.append(tmp_2 - tmp_1)
                elif token == '*':
                    stk.append(tmp_2 * tmp_1)
                elif token == '/':
                    # 题目要求保留整数除法的整数部分，因此不能用python 的'//'向下整除在负数时候回小1
                    stk.append(tmp_2 / tmp_1)
        return int(stk.pop(-1))

