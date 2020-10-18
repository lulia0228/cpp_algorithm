# -*- coding: utf-8 -*-


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        tmp_max = nums[0] # 表示当前步可以到达的最远处
        for i in range(len(nums)):
            # 剪枝作用
            if tmp_max == len(nums)-1:
                return True
            if i > tmp_max:
                return False
            tmp_max = max(tmp_max, nums[i]+i)
        return True