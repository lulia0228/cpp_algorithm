# -*- coding: utf-8 -*-

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        if m == 0 : return []
        n = len(matrix[0])
        lt, rt, up, down = 0, n-1, 0, m-1
        res =  []
        while True:
            for i in range(lt, rt+1):
                res.append(matrix[up][i])
            up += 1
            if up > down: break
            for i in range(up, down+1):
                res.append(matrix[i][rt])
            rt -= 1
            if rt < lt: break
            for i in range(rt, lt-1, -1):
                res.append(matrix[down][i])
            down -= 1
            if down < up: break
            for i in range(down, up-1, -1):
                res.append(matrix[i][lt])
            lt += 1
            if lt > rt: break
        return res
