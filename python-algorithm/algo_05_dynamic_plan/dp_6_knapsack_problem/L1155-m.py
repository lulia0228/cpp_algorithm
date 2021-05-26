#--coding:utf-8--

class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        #动态规划  背包问题
        dp = [[0 for _ in range(target + 1)] for _ in range(d + 1)]
        dp[0][0] = 1
        for i in range(1, d + 1):           #虚指
            for j in range(i, target + 1):  #因为投出来的最小数是1
                for k in range(1, min(f, j) + 1):   #第i个扔出来的值
                    dp[i][j] += dp[i-1][j-k]
                    dp[i][j] %= 1000000007
        return dp[d][target]
