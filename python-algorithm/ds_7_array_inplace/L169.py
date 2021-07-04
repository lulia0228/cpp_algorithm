# -*- coding: utf-8 -*-

# 169 多数元素
# 进阶要求线性时间复杂度 常数空间复杂度 就不太好做了
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        flag= nums[0]
        cnt = 1
        # 摩尔投票
        for i in range(1, len(nums)):
            if nums[i] != flag:
                cnt -= 1
                if cnt == 0:
                    flag = nums[i]
                    cnt = 1 # 容易漏掉
            else:
                cnt += 1
        return flag

# 排序
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]