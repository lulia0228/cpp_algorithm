#--coding:utf-8--
'''
@Time   : 2020/10/10
@Author : No Name
'''

# 现有n个物品，每个的重量用数组w表示，每个物品的价值用数组v表示，
# 现在一个背包最大承重为C，求用这n个物品装入背包能获得的最大价值？

class Solution:
    def knapsack(self, w , v , C ):
        n = len(w)
        # dp[i][j]表示用[0,...,i-1]物品填充容量为j的最大价值
        dp = [[0]*(C+1) for i in range(n+1)]
        for i in range(1, n):
            for j in range(C+1):
                # 装或者不装第i个
                if j >= w[i]:
                    dp[i][j] = max(dp[i-1][j], v[i-1]+dp[i-1][j - w[i-1]])
                else:
                    dp[i][j] = dp[i-1][j]  # 不装第i个
        return dp[n][C]
