# -*- coding: utf-8 -*-
# @Time    : 2020/10/4 10:06
# @Author  : No Name

# 先转置矩阵，再对称交换所有列
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(i, n):
                if j > i:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n // 2):
            for j in range(m):
                matrix[j][i], matrix[j][n - i - 1] = matrix[j][n - i - 1], matrix[j][i]
