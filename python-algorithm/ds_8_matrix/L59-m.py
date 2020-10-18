# -*- coding: utf-8 -*-


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for i in range(n)] for i in range(n)]
        cnt = 1
        m, n = len(matrix), len(matrix[0])
        up, down, left, right = 0, m - 1, 0, n - 1
        while up <= down:
            if cnt <= m * n:
                for i in range(left, right + 1):
                    matrix[up][i] = cnt
                    cnt += 1
            up += 1
            if cnt <= m * n:
                for i in range(up, down + 1):
                    matrix[i][right] = cnt
                    cnt += 1
            right -= 1
            if cnt <= m * n:
                for i in range(right, left - 1, -1):
                    matrix[down][i] = cnt
                    cnt += 1
            down -= 1
            if cnt <= m * n:
                for i in range(down, up - 1, -1):
                    matrix[i][left] = cnt
                    cnt += 1
            left += 1
        return matrix


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for i in range(n)] for i in range(n)]
        m, n = len(matrix), len(matrix[0])
        cnt = 1
        up, down, left, right = 0, m - 1, 0, n - 1
        while True:
            # 往右
            for i in range(left, right + 1):
                matrix[up][i] = cnt
                cnt += 1
            if up >= down: break
            up += 1
            # 往下
            for i in range(up, down + 1):
                matrix[i][right] = cnt
                cnt += 1
            if right <= left: break
            right -= 1
            # 往左
            for i in range(right, left - 1, -1):
                matrix[down][i] = cnt
                cnt += 1
            if down <= up: break
            down -= 1
            # 往上
            for i in range(down, up - 1, -1):
                matrix[i][left] = cnt
                cnt += 1
            if left >= right: break
            left += 1
        return matrix