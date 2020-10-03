# -*- coding: utf-8 -*-
# @Time    : 2020/10/3 13:59
# @Author  : No Name


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        i = 0
        while i<len(nums):
            tmp_len = 0
            while i<len(nums) and nums[i] == 1:
                tmp_len += 1
                i += 1
            if tmp_len != 0:
                res = max(res, tmp_len)
            else:
                i += 1
        return res

    
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        tmp_len = 0
        for n in nums:
            if n == 0:
                res = max(res, tmp_len)
                tmp_len = 0
            else:
                tmp_len += 1
        return max(res, tmp_len) # 不是以0结尾的时候最后一次tmp要额外处理

