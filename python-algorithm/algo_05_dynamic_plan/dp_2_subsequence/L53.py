#--coding:utf-8--
'''
@Time   : 2020/10/9
@Author : No Name
'''

# dp[i] = max(dp[i-1]+nums[i], nums[i])
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        final_sum = nums[0]
        dp = [0]*len(nums)
        # dp[i]代表的是以当前元素为结尾的连续子数组的最大和
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            final_sum = max(final_sum, dp[i])
        return final_sum


# 观察状态转移方程，发现，只用到了上一个元素，考虑优化空间
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        final_sum = nums[0]
        tmp_max = nums[0]
        for i in range(1, len(nums)):
            tmp_max = max(tmp_max+nums[i], nums[i])
            final_sum = max(final_sum, tmp_max)
        return final_sum