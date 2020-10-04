# -*- coding: utf-8 -*-
# @Time    : 2020/10/4 10:44
# @Author  : No Name

# 占用了额外的空间，题目进阶要求额外空间为1
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        row_flag = set()
        col_flag = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row_flag.add(i)
                    col_flag.add(j)
        for i in row_flag:
            for j in range(n):
                matrix[i][j] = 0
        for j in col_flag:
            for i in range(m):
                matrix[i][j] = 0

# 不使用额外空间
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        # 1 先标记处第一列是否有0
        flag_col0 = False
        for i in range(m):
            if matrix[i][0] == 0:
                flag_col0 = True
                break
        # 2 用每行第一个数字标记该行是否有0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    break
        # 3 从第二列开始，用各列第一个数字标记该列是否有0
        for j in range(1, n):
            for i in range(m):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
        # 4 先不处理第一行 第一列 会对别的列产生干扰
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        # 5 现在处理第一行
        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0
        # 6 现在处理第一列
        if flag_col0:
            for i in range(m):
                matrix[i][0] = 0

