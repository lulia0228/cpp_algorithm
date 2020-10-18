# -*- coding: utf-8 -*-

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        d = {}
        res = 0
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1
        for i in range(len(nums)):
            if nums[i]-1 in d:
                res = max(res, d[nums[i]]+d[nums[i]-1])
            if nums[i]+1 in d:
                res = max(res, d[nums[i]]+d[nums[i]+1])
        return res