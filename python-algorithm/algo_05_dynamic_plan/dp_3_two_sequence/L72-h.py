#--coding:utf-8--
'''
@Time   : 2020/10/9
@Author : No Name
'''

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        sz1, sz2 = len(word1), len(word2)
        # dp[i][j]表示从word1[0:i]转移到word2[0:j]  数组/字符串切片代表前闭后开
        # 比如dp[1][1]表示的是从word1第一个字母转移到word2第1个字母
        dp = [[0]*(sz2+1) for i in range(sz1+1)]
        for j in range(sz2+1):
            dp[0][j] = j # word1添加i个字母
        for i in range(sz1+1):
            dp[i][0] = i # word1删除i个字母
        for i in range(1, sz1+1):
            for j in range(1, sz2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(min(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1])+1
        return dp[sz1][sz2]


# 优化空间
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        sz1, sz2 = len(word1), len(word2)
        # dp[i][j]表示从word1[0:i]转移到word2[0:j]  数组/字符串切片代表前闭后开
        # 比如dp[1][1]表示的是从word1第一个字母转移到word2第1个字母
        dp = [[0]*(sz2+1) for i in range(2)]
        for j in range(sz2+1):
            dp[0][j] = j # word1添加i个字母
        for i in range(1, sz1+1):
            for j in range(sz2+1):
                if j == 0:
                    dp[1][j] = i
                    continue
                if word1[i-1] == word2[j-1]:
                    dp[1][j] = dp[0][j-1]
                else:
                    dp[1][j] = min(min(dp[0][j], dp[1][j-1]), dp[0][j-1])+1
            # dp[0] = dp[1] # 不能这么干，会整体引用原来的第二行，一旦原来的第二行变化，第一行会自动改变
            for i in range(sz2+1):
                dp[0][i] = dp[1][i]
        return dp[0][sz2]


