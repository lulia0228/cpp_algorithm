# -*- coding: utf-8 -*-

# 同leetcode 54

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        m = len(matrix)
        if m == 0:
            return res
        n = len(matrix[0])

        up, down, left, right = 0, m-1, 0, n-1
        while True:
            for i in range(left, right+1):
                res.append(matrix[up][i])
            up += 1
            if up > down: break

            for i in range(up, down+1):
                res.append(matrix[i][right])
            right -= 1
            if right < left: break

            for i in range(right, left-1,-1):
                res.append(matrix[down][i])
            down -= 1
            if down < up : break

            for i in range(down, up-1, -1):
                res.append(matrix[i][left])
            left += 1
            if left > right: break

        return res


