#--coding:utf-8--

# 单调栈
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        sz = len(prices)
        res = prices
        stk = [0]
        for i in range(1, sz):
            while stk and prices[i]<=prices[stk[-1]]:
                idx = stk.pop()
                res[idx] = prices[idx]-prices[i]
            stk.append(i)
        return res