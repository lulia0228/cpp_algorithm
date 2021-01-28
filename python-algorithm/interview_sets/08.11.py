#--coding:utf-8--
class Solution:
    def waysToChange(self, n: int) -> int:
        candiate = [25,10,5,1]
        dp = [0]*(n+1)
        dp[0] = 1
        for coin in candiate:
            for i in range(coin, n+1, 1):
                dp[i] += dp[i-coin]
        return dp[n]%1000000007
