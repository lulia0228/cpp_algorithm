#--coding:utf-8--

class Solution:
    def divideNumber(self , n , k ):
        # write code here
        dp = [[0]*(k+1) for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1,n+1):
            for j in range(1,k+1):
                if i-j >= 0:
                    # 两种情况，用i-1个数划分成j-1份 ； 用i-j个数划分成j份
                    dp[i][j] = dp[i-1][j-1] + dp[i-j][j]
        return dp[n][k]