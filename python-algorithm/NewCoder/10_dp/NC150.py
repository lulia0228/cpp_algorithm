# -*- coding: utf-8 -*-
class Solution:
    def numberOfTree(self , n ):
        # write code here
        dp = [0]*(n+1)
        dp[0] = dp[1] = 1
        for i in range(2, n+1):
            for j in range(1,i+1):
                dp[i] += dp[j-1]*dp[i-j]
                dp[i] %= 1000000007
        return dp[n]

n = 100000
res = Solution().numberOfTree(n)
print(res)

