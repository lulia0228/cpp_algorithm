# -*- coding: utf-8 -*-


# 利用值和下标的异或运算
# 0-n每个值和下标异或，缺少的下标是n
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            res ^= nums[i]
            res ^= i
        return res^len(nums)