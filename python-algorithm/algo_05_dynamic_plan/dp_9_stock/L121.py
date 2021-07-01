#--coding:utf-8--

# 题目要求只能交易一次

# 这里提供两种方法：一种是把每天当做卖出日期，选择这一天前面的所有天中的最低价格当做卖出日期；
# 另一种是动态规划，不过需要先抽象问题，有两种抽象方式
# （1）转化为求价格差值序列的最大子序列和问题。
# （2）转化成二维状态转移问题

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sz = len(prices)
        # 第i天结束持有(1)/不持有(0)的最大利润
        dp = [[0]*2 for _ in range(sz)]

        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, sz):
            # 昨天不持有，今天不买；昨天持有今天卖出
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            # 昨天不持有，今天买；昨天持有，今天不卖
            dp[i][1] = max(-prices[i], dp[i-1][1])

        return dp[sz-1][0]

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0
        profits = [prices[i]-prices[i-1] for i in range(1, len(prices))]
        tmp_max = max(0, profits[0])
        final_max = max(0, tmp_max)
        for i in range(1, len(profits)):
            # 第i天卖出的最大利润等于第i-1天卖出的最大利润+利润差
            tmp_max = max(tmp_max+profits[i], 0)
            final_max = max(final_max, tmp_max)
        return final_max


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        min_p = prices[0]
        for i in range(1, len(prices)):
            min_p = min(min_p, prices[i])
            res =  max(res, prices[i]-min_p)
        return res