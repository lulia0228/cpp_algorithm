# -*- coding: utf-8 -*-

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        flag = nums[0]
        cnt = 0
        for i in range(len(nums)):
            if cnt == 0:
                flag = nums[i]
                cnt= 1
            else:
                if nums[i] != flag:
                    cnt -= 1
                else:
                    cnt += 1
        return flag