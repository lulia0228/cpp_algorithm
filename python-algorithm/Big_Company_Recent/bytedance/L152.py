# -*- coding: utf-8 -*-

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        sz = len(nums)
        if sz == 0: return 0
        tmp_min, tmp_max = nums[0], nums[0]
        final_max = nums[0]
        for i in range(1, sz):
            temp = tmp_min
            tmp_min = min(min(tmp_max*nums[i], tmp_min*nums[i]),nums[i])
            tmp_max = max(max(tmp_max*nums[i], temp*nums[i]),nums[i])
            final_max = max(tmp_max, final_max)
        return final_max

