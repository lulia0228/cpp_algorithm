#--coding:utf-8--

# 同lc516

class Solution:
    def longestPalindromeSubSeq(self , s ):
        # write code here
        sz = len(s)
        dp = [[0]*sz for _ in range(sz)]
        for k in range(sz):
            dp[k][k] = 1
        for i in range(sz):
            for j in range(i-1, -1, -1):
                if s[i] == s[j]:
                    dp[j][i] = dp[j+1][i-1]+2
                else:
                    dp[j][i] = max(dp[j+1][i], dp[j][i-1])
        return dp[0][sz-1]
