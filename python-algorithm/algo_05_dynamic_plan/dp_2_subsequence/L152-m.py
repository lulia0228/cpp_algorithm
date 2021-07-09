#--coding:utf-8--

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        tmp_max = nums[0]
        tmp_min = nums[0]
        final_max = nums[0]
        for i in range(1, len(nums)):
            # 标记上一步的最大值，防止被下面覆盖丢失
            tmp = tmp_max
            tmp_max = max(nums[i], max(tmp_max*nums[i], tmp_min*nums[i]))
            tmp_min = min(nums[i], min(tmp*nums[i], tmp_min*nums[i]))
            final_max = max(final_max, tmp_max)
        return final_max
