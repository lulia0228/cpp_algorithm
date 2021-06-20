#--coding:utf-8--
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 计算01背包问题的结果
# @param V int整型 背包的体积
# @param n int整型 物品的个数
# @param vw int整型二维数组 第一维度为n,第二维度为2的二维数组,vw[i][0],vw[i][1]分别描述i+1个物品的vi,wi
# @return int整型
#

# dp[i][j] 用前i个数(0~i-1)装满体积j的最大重量

class Solution:
    def knapsack(self , V , n , vw ):
        # write code here
        dp = [[0]*(V+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, V+1):
                if vw[i-1][0] <= j:
                    # 装或者不装i-1
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-vw[i-1][0]]+vw[i-1][1])
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][V]