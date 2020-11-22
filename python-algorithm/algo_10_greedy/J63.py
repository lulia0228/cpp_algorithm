#--coding:utf-8--


# 同leetcode121

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == []:
            return 0
        p = [prices[i]-prices[i-1] for i in range(1,len(prices))]
        cur_max = max(0, p[0])
        final_max = max(0, p[0])
        for i in range(1, len(p)):
            cur_max = max(cur_max+p[i], 0)
            final_max = max(final_max, cur_max)
        return final_max