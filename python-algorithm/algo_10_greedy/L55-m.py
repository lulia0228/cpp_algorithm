# -*- coding: utf-8 -*-

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        fast_arrive = 0
        for i, step in enumerate(nums):
            if fast_arrive>=len(nums)-1:# 提前结束；剪枝
                return True
            if fast_arrive<i:
                return False
            fast_arrive = max(fast_arrive, nums[i]+i)
        return True
