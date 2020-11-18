#--coding:utf-8--

# 二维矩阵查找；同leetcode 240

class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == []:
            return False
        m, n = len(matrix), len(matrix[0])
        i,j = m-1, 0
        while i>=0 and j<n:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                j += 1
            else:
                i -= 1
        return False