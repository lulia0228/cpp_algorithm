#--coding:utf-8--
'''
@Time   : 2020/10/10
@Author : No Name
'''

# dp[i][j]表示A[0:i]和B[0:j]以两个数组的最后一个数字作为结尾的最长公共子数组的长度   数组/字符串切片代表前闭后开

class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        res = 0
        m, n = len(A), len(B)
        dp = [[0] * (n + 1) for i in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    res = max(res, dp[i][j])
                else:
                    dp[i][j] = 0
        return res


# 两行空间存储
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        res = 0
        m, n = len(A), len(B)
        dp = [[0] * (n + 1) for i in range(2)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    dp[1][j] = dp[0][j - 1] + 1
                    res = max(res, dp[1][j])
                else:
                    dp[1][j] = 0
            for i in range(n + 1):
                dp[0][i] = dp[1][i]
        return res
