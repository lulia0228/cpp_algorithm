# -*- coding: utf-8 -*-
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        r_dic = {}
        for i in range(len(nums)):
            find = target - nums[i]
            if find in r_dic:
                return [r_dic[find], i]
            else:
                r_dic[nums[i]] = i
