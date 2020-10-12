#--coding:utf-8--
'''
@Time   : 2020/10/12
@Author : No Name
'''

# 这里提供两种方法：一种是把每天当做卖出日期，选择这一天前面的所有天中的最低价格当做卖出日期；
# 另一种是动态规划，不过需要先抽象问题，转化为求价格差值序列的最大子序列和问题。

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        new_arr = [prices[i+1]-prices[i] for i in range(len(prices)-1)]
        cur_max = max(new_arr[0], 0)
        final_max = max(new_arr[0], 0)
        for i in range(1, len(new_arr)):
            cur_max = max(cur_max+new_arr[i],0)
            final_max = max(final_max, cur_max)
        return final_max


# 超时
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(1, len(prices)):
            for j in range(i):
                res =  max(res, prices[i]-prices[j])
        return res