# -*- coding: utf-8 -*-

# 滑动窗口，有时候结果是在收缩窗口的内部处理的，有时候是在收缩完窗口外面完成的
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i, j = 0, 0
        t_sum = 0
        ans = len(nums)+1
        while j < len(nums):
            t_sum += nums[j]
            while t_sum>=target:
                ans = min(ans, j-i+1)
                t_sum -= nums[i]
                i += 1
            j += 1
        return 0 if ans==len(nums)+1 else ans
