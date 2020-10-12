#--coding:utf-8--
'''
@Time   : 2020/10/12
@Author : No Name
'''

class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0]*(num+1)
        for i in range(1, num+1):
            dp[i] = dp[i//2] + (1&i)
        return dp