#--coding:utf-8--



# 动态规划思想提交后速度比较慢，贪心算法是最快的
# dp[1] 原来就有不需要操作 dp[1]=0
# dp[2] 复制1次A，再粘贴1次A 共2次操作 dp[2]=2

class Solution:
    def minSteps(self, n: int) -> int:
        dp = [i for i in range(n+1)]
        dp[1] = 0
        for i in range(2, n+1):
            for j in range(2, i):
                if i%j == 0:
                    # i/j = [1次复制+（i/j-1)次粘贴操作]
                    dp[i] = min(dp[i], dp[j]+int(i//j))
        return dp[n]