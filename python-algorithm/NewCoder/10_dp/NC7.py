# -*- coding: utf-8 -*-

# 贪心做的；动态规划怎么做呢

class Solution:
    def maxProfit(self , prices ):
        # write code here
        min_v = prices[0]
        res = 0
        for p in prices:
            min_v = min(min_v, p)
            res = max(res, p-min_v)
        return res