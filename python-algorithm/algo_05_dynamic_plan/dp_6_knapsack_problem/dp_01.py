#--coding:utf-8--


# 现有n个物品，每个的重量用数组w表示，每个物品的价值用数组v表示，
# 现在一个背包最大承重为C，求用这n个物品装入背包能获得的最大价值？

class Solution:
    def knapsack(self, w , v , C ):
        n = len(w)
        # dp[i][j]表示用[0,...,i-1]物品填充容量为j的最大价值
        dp = [[0]*(C+1) for i in range(n+1)]
        for i in range(1, n+1):
            for j in range(C+1):
                # 装或者不装第i个
                if j >= w[i]:
                    dp[i][j] = max(dp[i-1][j], v[i-1]+dp[i-1][j - w[i-1]])
                else:
                    dp[i][j] = dp[i-1][j]  # 不装第i个
        return dp[n][C]

# 省空间的写法
class Solution:
    def knapsack(self, w , v , C ):
        n = len(w)
        dp = [0]*(C+1)
        for i in range(n):
            # 为了省空间，只用1维表达，只有倒着设计才能避免覆盖的问题
            # 因为dp[j-w]表示的是dp[i-1][j-w]，正着计算，省略有维度，会被二维的d[i][j-w]覆盖
            for j in range(C, w[i-1]-1, -1):
                dp[j] = max(dp[j], v[i]+dp[j - w[i]])
        return [C]
