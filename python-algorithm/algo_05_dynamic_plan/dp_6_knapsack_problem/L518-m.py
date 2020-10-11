# -*- coding: utf-8 -*-
# @Time    : 2020/10/11 17:07
# @Author  : No Name

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        sz = len(coins)
        dp = [0]*(amount+1)
        dp[0] = 1
        for coin in coins:
            for i in range(1, amount+1):
                if i >= coin:
                    dp[i] += dp[i-coin]
        return dp[amount]

