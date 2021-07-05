# -*- coding: utf-8 -*-


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        grid = [[0] * n for _ in range(n)]
        cnt = 1
        up, down, lt, rt = 0, n - 1, 0, n - 1
        while True:
            for i in range(lt, rt + 1, 1):
                grid[up][i] = cnt
                cnt += 1
            up += 1
            if up > down: break

            for i in range(up, down + 1, 1):
                grid[i][rt] = cnt
                cnt += 1
            rt -= 1
            if rt < lt: break

            for i in range(rt, lt - 1, -1):
                grid[down][i] = cnt
                cnt += 1
            down -= 1
            if down < up: break

            for i in range(down, up - 1, -1):
                grid[i][lt] = cnt
                cnt += 1
            lt += 1
            if lt > rt: break
        return grid