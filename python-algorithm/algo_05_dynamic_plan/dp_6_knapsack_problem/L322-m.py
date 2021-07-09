# -*- coding: utf-8 -*-


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1]*(amount+1)
        dp[0] = 0
        # 和硬币找零II不同，这里内外层可以调换
        for coin in coins:
            for c in range(coin, amount+1):
                dp[c] = min(dp[c], dp[c-coin]+1)
        return dp[amount] if dp[amount]!=amount+1 else -1