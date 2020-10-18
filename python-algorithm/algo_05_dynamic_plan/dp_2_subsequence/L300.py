#--coding:utf-8--


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        final_max = 1
        # dp[i]表示以nums[i]为结尾的上升子序列的最大长度
        dp = [1]*len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
            final_max = max(final_max, dp[i])
        return final_max