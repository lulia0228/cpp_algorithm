# -*- coding: utf-8 -*-
# @Time    : 2020/10/7 10:28
# @Author  : No Name

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            res ^= nums[i]
        return res

