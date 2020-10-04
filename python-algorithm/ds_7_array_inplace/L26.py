# -*- coding: utf-8 -*-
# @Time    : 2020/10/4 15:31
# @Author  : No Name

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        flag = nums[0]
        cnt = 0
        for i in range(len(nums)):
            if nums[i] != nums[cnt]:
                cnt += 1
                nums[cnt] = nums[i]
        return cnt+1