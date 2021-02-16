# -*- coding: utf-8 -*-

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_min = prices[0]
        final_max = 0
        for i in range(len(prices)):
            # 记录当前步的最小值
            cur_min = min(cur_min, prices[i])
            final_max = max(final_max, prices[i]-cur_min)
        return final_max


# 模仿最大连续子序列和
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0
        subSum = [prices[i]-prices[i-1] for i in range(1, len(prices))]
        tmp_max = max(0, subSum[0])
        final_max = tmp_max
        for i in range(1, len(subSum)):
            tmp_max = max(tmp_max+subSum[i], 0)
            final_max = max(final_max, tmp_max)
        return final_max