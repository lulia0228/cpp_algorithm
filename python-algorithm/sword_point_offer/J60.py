# -*- coding: utf-8 -*-


# n个骰子掷出来的点数组合种类

# 动态规划：n个骰子掷出来j点的组合种类数等于n-1个骰子掷出来j-i点的组合种类数之和（i从1~6）
# 即dp[n][j] = dp[n-1][j-1] + dp[n-1][j-2]+...dp[n-1][j-6]

class Solution:
    def dicesProbability(self, n: int):
        dp = [[0]*(6*n+1)  for i in range(n+1)]
        for i in range(1,7):
            dp[1][i] = 1
        for i in range(2, n+1):
            for j in range(i*1, i*6+1):
                for m in range(1,7):
                    if j-m >= i-1:
                        dp[i][j] += dp[i-1][j-m]
        res = [item/float(pow(6,n)) for item in dp[n][n:6*n+1]]
        return res

res = Solution().dicesProbability(3)
print(res)


# 压缩到2行空间；其实还可以压缩到1行空间（倒序更新）
class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        dp = [[0]*(6*n+1)  for i in range(2)]
        for i in range(1,7):
            dp[0][i] = 1
        for i in range(2, n+1):
            for j in range(i*1, 6*i+1):
                for m in range(1,7):
                    if j-m >= i-1:
                        dp[1][j] += dp[0][j-m]
            for j in range(6*n+1):
                dp[0][j] = dp[1][j]
                dp[1][j] = 0  # 必须要清0；否则会累加
        print(dp)
        res = [item/float(pow(6,n)) for item in dp[0][n:6*n+1]]
        return res