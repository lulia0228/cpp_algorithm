# -*- coding: utf-8 -*-
class Solution:
    def numberOfTree(self , n ):
        # write code here
        dp = [0]*(n+1)
        dp[0] = dp[1] = 1
        for i in range(2, n+1):
            for k in range(1, i+1):
                dp[i] += dp[k-1]*dp[i-k]
                dp[i] = dp[i]%1000000007
        return dp[n]

print(Solution().numberOfTree(10000)) # 512319131