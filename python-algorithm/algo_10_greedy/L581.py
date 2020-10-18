# -*- coding: utf-8 -*-

# 这道题不好O(n) O(1)的方法不好想到
# 1  排序 O(nlogn) O(n)
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        start = len(nums)-1
        end = 0
        ref = sorted(nums)
        for i in range(len(nums)):
            if nums[i] != ref[i]:
                start = min(start, i)
                end = max(end, i)
        return end-start+1 if start<end else 0

# 2  O(n) O(1)

