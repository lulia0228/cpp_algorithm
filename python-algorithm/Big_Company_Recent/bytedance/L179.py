# -*- coding: utf-8 -*-

from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums.sort(key=cmp_to_key(self.custom_sort), reverse=True)
        if nums[0] == 0:
            return '0'
        return "".join([str(i) for i in nums])

    def custom_sort(self, x,y):
        if int(str(x)+str(y)) > int(str(y)+str(x)):
            return 1
        else:
            return -1

