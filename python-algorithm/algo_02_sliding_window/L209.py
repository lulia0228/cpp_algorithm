# -*- coding: utf-8 -*-
# @Time    : 2020/9/19 15:13
# @Author  : Heng Li
# @File    : L209.py
# @Software: PyCharm

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        lt, rt = 0, 0
        res = len(nums) + 1
        tmp_sum = 0
        while rt < len(nums):
            tmp_sum += nums[rt]
            while tmp_sum >= s:
                tmp_sum -= nums[lt]
                res = min(res, rt-lt+1)
                lt += 1
            rt += 1
        return 0 if res > len(nums) else res