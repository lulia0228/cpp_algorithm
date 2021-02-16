# -*- coding: utf-8 -*-
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i, j = 0, 0
        sum_ = 0
        min_len = len(nums) + 1
        while j < len(nums):
            sum_ += nums[j]
            while sum_ >= target:
                min_len = min(min_len, j - i + 1) # 注意这句的位置
                sum_ -= nums[i]
                i += 1
            j += 1
        return 0 if min_len == len(nums) + 1 else min_len

