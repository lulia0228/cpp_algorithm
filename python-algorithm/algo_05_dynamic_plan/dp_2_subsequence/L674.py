#--coding:utf-8--
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        tmp_max = 1
        final_max = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                tmp_max += 1
            else:
                tmp_max = 1
            final_max = max(tmp_max, final_max)
        return final_max

# class Solution:
#     def findLengthOfLCIS(self, nums: List[int]) -> int:
#         dp = [1]*len(nums)
#         res = 1
#         for i in range(1, len(nums)):
#             if nums[i]>nums[i-1]:
#                 dp[i] = dp[i-1]+1
#                 res = max(res, dp[i])
#         return res