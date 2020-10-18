# -*- coding: utf-8 -*-


# 使用遍历个数作为终止条件
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix == []:
            return []
        res = []
        cnt = 0
        m, n = len(matrix), len(matrix[0])
        up, down, left, right = 0, m - 1, 0, n - 1
        while up <= down:
            if cnt < m * n:
                for i in range(left, right + 1):
                    res.append(matrix[up][i])
                    cnt += 1
            up += 1
            if cnt < m * n:
                for i in range(up, down + 1):
                    res.append(matrix[i][right])
                    cnt += 1
            right -= 1
            if cnt < m * n:
                for i in range(right, left - 1, -1):
                    res.append(matrix[down][i])
                    cnt += 1
            down -= 1
            if cnt < m * n:
                for i in range(down, up - 1, -1):
                    res.append(matrix[i][left])
                    cnt += 1
            left += 1
        return res


# 在遍历的过程中根据索引退出循环
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix == []:
            return []
        res = []
        m, n = len(matrix), len(matrix[0])
        up, down, left, right = 0, m - 1, 0, n - 1
        while True:
            # 往右
            for i in range(left, right + 1):
                res.append(matrix[up][i])
            if up >= down: break
            up += 1
            # 往下
            for i in range(up, down + 1):
                res.append(matrix[i][right])
            if right <= left: break
            right -= 1
            # 往左
            for i in range(right, left - 1, -1):
                res.append(matrix[down][i])
            if down <= up: break
            down -= 1
            # 往上
            for i in range(down, up - 1, -1):
                res.append(matrix[i][left])
            if left >= right: break
            left += 1
        return res

