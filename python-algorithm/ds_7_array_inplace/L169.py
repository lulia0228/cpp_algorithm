# -*- coding: utf-8 -*-
# @Time    : 2020/10/4 15:47
# @Author  : No Name

# 进阶要求线性时间复杂度 常数空间复杂度 就不太好做了
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = nums[0]
        cnt = 0
        for i in range(len(nums)):
            if cnt == 0:
                res = nums[i]
                cnt = 1
            else:
                if nums[i] != res:
                    cnt -= 1
                else:
                    cnt += 1
        return res