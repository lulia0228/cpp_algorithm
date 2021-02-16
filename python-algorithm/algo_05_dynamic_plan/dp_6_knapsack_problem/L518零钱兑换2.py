# -*- coding: utf-8 -*-

# 动态规划
# 这道题不要去想背包问题，直接想DP就好了
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1)
        dp[0] = 1
        for coin in coins:
            for i in range(1, amount+1):
                dp[i] += (dp[i-coin]  if i>=coin else 0)
        return dp[amount]

