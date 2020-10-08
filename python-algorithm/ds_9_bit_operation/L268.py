# -*- coding: utf-8 -*-
# @Time    : 2020/10/7 11:47
# @Author  : No Name

# 利用值和下标的异或运算
# 0-n每个值和下标异或，缺少的下标是n
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            res = res ^ i ^ nums[i]
        return res^len(nums)