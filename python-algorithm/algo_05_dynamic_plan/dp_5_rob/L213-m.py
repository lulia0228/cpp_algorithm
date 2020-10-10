#--coding:utf-8--
'''
@Time   : 2020/10/10
@Author : No Name
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        max1, max2 = self.rob_(nums[:n-1]), self.rob_(nums[1:])
        return max(max1, max2)

    def rob_(self, nums):
        m = len(nums)
        dp = [0]*(m+1)
        for i in range(1, m+1):
            dp[i] = max(dp[i-1], nums[i-1]+(0 if i<2 else dp[i-2]))
        return dp[m]