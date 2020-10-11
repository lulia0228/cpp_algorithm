#--coding:utf-8--
'''
@Time   : 2020/10/10
@Author : No Name
'''

# 多维费用背包：物品不仅有重量，还有体积，同时考虑这两种限制
# 二维费用背包问题。m和n是两个维度的约束(相当于背包问题中的体积约束，只不过增加了一个维度)。

# 这道题的2个约束是 字符0、1各自的使用约束 目标是可以生成的指定出现在指定集合中的字符串数量最多

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp=[[0]*(n+1) for _ in range(m+1)]
        for item in strs:
            count_0 = item.count("0")
            count_1 = item.count("1")
            for i in range(m,count_0 -1,-1):
                for j in range(n,count_1 -1,-1):
                    dp[i][j] = max(dp[i][j], 1+dp[i-count_0][j-count_1])
        return dp[m][n]
