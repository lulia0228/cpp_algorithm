# -*- coding: utf-8 -*-
# 原地哈希（所有元素都先加1，就可以统一写）
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] += 1
        for num in nums:
            # 直接原地修改元素为负值来标记是否被另外一个元素访问过
            # 因此这里的num一定要取绝对值
            index = abs(num)-1
            val = nums[index]
            if val < 0:
                # 如果元素值为负数，说明之前存在同一个值为abs(num)的元素
                return abs(num)-1
            # 原地修改访问标志
            nums[index] = -nums[index]

# 原地哈希，0元素特殊对待也可以
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        for n in nums:
            idx = abs(n)
            if nums[idx]<0 or nums[idx]==len(nums):
                return idx
            if idx==0:
                nums[idx] = len(nums)
            else:
                nums[idx] = -nums[idx]