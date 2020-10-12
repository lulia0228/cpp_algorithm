#--coding:utf-8--
'''
@Time   : 2020/10/12
@Author : No Name
'''

# 贪心算法：1 只要明天价格大于当天价格，当天就买；2 当天买第二天就卖
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)-1):
            res += max(prices[i+1]-prices[i], 0)
        return res


