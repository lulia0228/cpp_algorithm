# -*- coding: utf-8 -*-
# 除自身以外的乘积数组
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        for i in range(1, len(nums)):
            res[i] = res[i-1]*nums[i-1]
        temp = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= temp
            temp *= nums[i]
        return res
