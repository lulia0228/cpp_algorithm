#--coding:utf-8--


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        final_max = nums[0]
        cur_max = nums[0]
        for i in range(1, len(nums)):
            cur_max = max(cur_max+nums[i], nums[i])
            final_max = max(final_max, cur_max)
        return final_max

