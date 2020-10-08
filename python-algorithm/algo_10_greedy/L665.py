# -*- coding: utf-8 -*-
# @Time    : 2020/10/7 19:51
# @Author  : No Name

# 在出现 nums[i]<nums[i-1] 时，需要考虑的是应该修改数组的哪个数，使得本次修改能使 i 之前的数组成为非递减数组，并且 不影响后续的操作
# 优先考虑令 nums[i-1] = nums[i]，因为如果修改nums[i] = nums[i-1]的话，那么nums[i]这个数会变大就有可能比nums[i+1] 大，
# 特殊情况：nums[i]<nums[i-1]&&nums[i]<nums[i-2]，修改 nums[i-1]=nums[i] 不能使数组成为非递减数组，只能修改 nums[i]=nums[i-1]。

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        cnt = 0
        for i in range(1, len(nums)):
            if cnt > 1:
                return False
            if nums[i] >= nums[i - 1]:
                continue
            cnt += 1
            # 以下为关键替换部分
            if i - 2 >= 0 and nums[i - 2] > nums[i]:
                nums[i] = nums[i - 1]
            else:
                nums[i - 1] = nums[i]

        return True if cnt <= 1 else False