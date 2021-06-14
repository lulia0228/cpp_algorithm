# -*- coding: utf-8 -*-
class Solution:
    def LCS(self , str1 , str2 ):
        # write code here
        m, n = len(str1), len(str2)
        end, max_len = 0, 0
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = 0
                if dp[i][j] > max_len:
                    end = j
                    max_len = dp[i][j]

        return str2[end-max_len:end]

