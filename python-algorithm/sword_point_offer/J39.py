# -*- coding: utf-8 -*-

# 同leetcode169

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        flag = nums[0]
        for i in range(len(nums)):
            if nums[i] == flag:
                cnt += 1
            else:
                if cnt == 0:
                    flag = nums[i]
                    cnt = 1
                else:
                    cnt -= 1
        return flag