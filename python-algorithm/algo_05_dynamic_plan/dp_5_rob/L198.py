#--coding:utf-8--
'''
@Time   : 2020/10/10
@Author : No Name
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        m = len(nums)
        dp = [0]*(m+1)
        for i in range(1, m+1):
            dp[i] = max(dp[i-1], nums[i-1]+(0 if i<2 else dp[i-2]))
        return dp[m]