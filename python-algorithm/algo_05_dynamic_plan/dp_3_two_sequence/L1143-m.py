#--coding:utf-8--
'''
@Time   : 2020/10/10
@Author : No Name
'''

# 和718最长重复子数组的区别在于，这里子序列不是连续的，只是相对顺序不变
#  dp[i][j]表示text1[0:i]和text2[0:j]的最长公共子序列的长度   数组/字符串切片代表前闭后开
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        # res = 0
        dp = [[0]*(n+1) for i in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                # res = max(res, dp[i][j])
        # return res
        return dp[m][n]

