# -*- coding: utf-8 -*-


# 503. 循环数组的下一个更大元素
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stk = []
        res = [-1 for i in range(len(nums))]
        for i in range(2 * len(nums) - 1):
            while stk != [] and nums[stk[-1]] < nums[i % len(nums)]:
                # 计算出栈元素的索引和当前遍历到的元素的索引的距离
                goal_idx = stk.pop(-1)
                res[goal_idx] = nums[i % len(nums)]
            if i < len(nums):
                stk.append(i)
        return res