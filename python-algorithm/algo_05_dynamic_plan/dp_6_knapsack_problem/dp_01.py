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
        # dp[i][j]表示用[0,...,i]物品填充容量为j的最大价值
        dp = [[-1]*(C+1) for i in range(n)]
        for j in range(C+1):
            dp[0][j] = (v[0] if j>w[0] else 0) # 即考虑第1个物品（索引是0）各个重量下的转态

        for i in range(1, n):
            for j in range(C+1):
                dp[i][j] = dp[i-1][j] # 先给其赋值不装第i个的状态
                if j >= w[i]:
                    dp[i][j] = max(dp[i][j], v[i]+dp[i-1][j - w[i]])
        return dp[n-1][C]
