# -*- coding: utf-8 -*-


# 占用了额外空间
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        record = [[] for i in range(m+n-1)]
        for i in range(m):
            for j in range(n):
                record[j-i+m-1].append(matrix[i][j])
        for diag in record:
            if len(set(diag)) != 1:
                return False
        return True

# 不占用额外空间
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False
        return True