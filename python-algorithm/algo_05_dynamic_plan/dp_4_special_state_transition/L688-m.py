#--coding:utf-8--

# 令 f[r][c][steps] 代表马在位置 (r, c) 移动了 steps 次以后还留在棋盘上的概率

# 使用二维的 dp 和 dp2 来存储我们的数据，而不是使用三维数组 f。
# dp2 代表 f[][][steps]，dp 代表 f[][][steps-1]。

class Solution(object):
    def knightProbability(self, N, K, r, c):
        dp = [[0] * N for _ in range(N)]
        dp[r][c] = 1
        for _ in range(K):
            dp2 = [[0] * N for _ in range(N)]
            for r, row in enumerate(dp):
                for c, val in enumerate(row):
                    for dr, dc in ((2,1),(2,-1),(-2,1),(-2,-1),
                                   (1,2),(1,-2),(-1,2),(-1,-2)):
                        if 0 <= r + dr < N and 0 <= c + dc < N:
                            dp2[r+dr][c+dc] += val / 8.0
            dp = dp2
        # print(dp)
        return sum(map(sum, dp))

