#--coding:utf-8--

# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
#
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
#
# 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1, n+1):
                if obstacleGrid[i-1][j-1] == 1:
                    dp[i][j] = 0
                else:
                    if i==1 and j==1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[m][n]