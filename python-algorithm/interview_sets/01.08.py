#--coding:utf-8--
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        col_0 = False
        for i in range(m):
            if matrix[i][0] == 0:
                col_0 = True
                break
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    break
        for j in range(1,n):
            for i in range(m):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    break
        for i in range(1,m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        for j in range(1,n):
            if matrix[0][0] == 0:
                matrix[0][j] = 0

        for i in range(m):
            if col_0:
                matrix[i][0] = 0


