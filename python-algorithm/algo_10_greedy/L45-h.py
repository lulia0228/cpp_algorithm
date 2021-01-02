# -*- coding: utf-8 -*-


class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        end = 0
        fartest = nums[0]
        for i in range(len(nums)-1):
            fartest = max(fartest, nums[i]+i)
            if end == i:
                jumps += 1
                end = fartest
        return jumps