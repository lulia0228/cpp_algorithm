#--coding:utf-8--

class Solution:
    def minEditCost(self , str1 , str2 , ic , dc , rc ):
        # write code here
        m, n = len(str1), len(str2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        dp[0][0] = 0
        for i in range(1,n+1):
            dp[0][i] = i*ic
        for j in range(1, m+1):
            dp[j][0] = i*dc
        for i in range(1,m+1):
            for j in range(1, n+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # (1) 先删掉str1的i-1位置，然后由str1[:i-1]变成str2[:j]
                    # (2) 先由str1[:i]变成str2[:j-1],然后在后面添加str2的j-1位置
                    # (3) 由str1[:i-1]变成str2[:j-1]然后替换str1的i-1位置值为str2的j-1位置值
                    dp[i][j] = min(min(dc+dp[i-1][j], dp[i][j-1]+ic), dp[i-1][j-1]+rc)
        return dp[m][n]