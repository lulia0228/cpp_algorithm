# -*- coding: utf-8 -*-

# dp[i][j] 表示在s[:i]的子序列中t[:j]出现的个数
# 边界情况：
# 当j=0时，t[:j]为空字符串，由于空字符串是任何字符串的子序列，因此对任意0≤i≤m，有dp[i][0]=1;
# 当i=0 且 j>0 时，s[:i]为空字符串，t[:j]为非空字符串，由于非空字符串不是空字符串的子序列，因此对任意0≤j<n，有dp[0][j]=0

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n:
            return 0

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    # 两种情况
                    # （1）t[:j]作为 s[:i]的子序列和
                    # （2）t[:j]作为 s[:i-1]的子序列 （即如果s[i-1]不参与匹配）
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    # 只能考虑t[:j] 作为 s[:i-1]的子序列的情况
                    dp[i][j] = dp[i - 1][j]

        return dp[m][n]
