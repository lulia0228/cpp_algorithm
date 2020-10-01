# -*- coding: utf-8 -*-
# @Time    : 2020/10/1 16:34
# @Author  : Heng Li
# @File    : L454-m.py
# @Software: PyCharm

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        d = {}
        lenth = len(A)
        res = 0
        for i in range(lenth):
            for j in range(lenth):
                tmp = A[i] + B[j]
                if tmp not in d:
                    d[tmp] = 1
                else:
                    d[tmp] += 1
        for m in range(lenth):
            for n in range(lenth):
                tmp = C[m] + D[n]
                if -tmp in d:
                    res += d[-tmp]
        return res