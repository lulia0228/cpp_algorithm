# -*- coding: utf-8 -*-
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        prefix = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = prefix[i][j - 1] + prefix[i - 1][j] - prefix[i - 1][j - 1] + mat[i - 1][j - 1]

        answer = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                min_i = max(0, i - k)
                max_i = min(m, i + k + 1)
                min_j = max(0, j - k)
                max_j = min(n, j + k + 1)
                # print(min_i, max_i, min_j, max_j)
                answer[i][j] = prefix[max_i][max_j] - prefix[max_i][min_j] - prefix[min_i][max_j] + prefix[min_i][min_j]

        return answer
