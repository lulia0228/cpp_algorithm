# -*- coding: utf-8 -*-

# 自底想上 动态规划；利用原来存储空间作为输出空间
class Solution(object):
    def minFallingPathSum(self, A):
        while len(A) >= 2:
            row = A.pop()
            for i in range(len(row)):
                A[-1][i] += min(row[max(0,i-1): min(len(row), i+2)])
        return min(A[0])