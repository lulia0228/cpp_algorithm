#--coding:utf-8--

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        sz = len(s)
        dp = [[0]*sz for i in range(sz)]
        for k in range(sz):
            dp[k][k] = 1
        for i in range(sz-1, -1, -1): # 必须倒着来，否则子问题不全
            for j in range(i+1, sz, 1):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][sz-1]