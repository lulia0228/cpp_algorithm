# -*- coding: utf-8 -*-

# 找出数组中重复的数组 和 leetcode448一样

class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] != i:
                # 循环终止条件
                while nums[i] != nums[nums[i]]:
                    tmp = nums[i]
                    nums[i], nums[tmp] = nums[tmp], nums[i]
                print(i, nums[i])

        for i in range(len(nums)):
            if nums[i] != i:
                return nums[i]

# 更快的做法
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while i != nums[i]:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                else:
                    tmp = nums[i]
                    nums[i], nums[tmp] = nums[tmp], nums[i]
        return -1