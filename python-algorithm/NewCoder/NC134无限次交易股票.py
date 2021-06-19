#--coding:utf-8--

# 贪心
class Solution:
    def maxProfit(self , prices ):
        # write code here
        res = 0
        for i in range(len(prices)-1):
            res += max(prices[i+1]-prices[i], 0)
        return res

# 动态规划
class Solution:
    def maxProfit(self , prices ):
        # write code here
        # dp[0]表示昨天不持有状态下获得的利润，dp[1]表示昨天持有状态下获得的利润
        dp = [0, -prices[0]]
        for i in range(1, len(prices)):
            tmp = dp[0]
            dp[0] = max(dp[0], dp[1]+prices[i])
            dp[1] = max(tmp-prices[i], dp[1])
        return dp[0]