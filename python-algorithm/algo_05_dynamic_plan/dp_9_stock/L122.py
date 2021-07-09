#--coding:utf-8--

# 同牛客134
# 题目要求不能同时参与多笔交易
class Solution:
    # #方法1 DP
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0, 0] for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][0]-prices[i], dp[i-1][1])
        return dp[len(prices)-1][0]

    # #方法2 贪心
    # def maxProfit(self, prices: List[int]) -> int:
    #     res = 0
    #     for i in range(1, len(prices)):
    #         res += max(prices[i]-prices[i-1], 0)
    #     return res