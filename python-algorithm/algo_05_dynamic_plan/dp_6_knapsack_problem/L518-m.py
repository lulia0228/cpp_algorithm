# -*- coding: utf-8 -*-

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1)
        dp[0] = 1
        # 内外层循环不能反，反了有重复计算
        for coin in coins:
            for c in range(coin, amount+1):
                dp[c] += dp[c-coin]
        return dp[amount]
