# -*- coding: utf-8 -*-



# 滑动窗口，有时候结果是在收缩窗口的内部处理的，有时候是在收缩完窗口外面完成的
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        lt, rt = 0, 0
        res = len(nums) + 1
        tmp_sum = 0
        while rt < len(nums):
            tmp_sum += nums[rt]
            while tmp_sum >= s:
                tmp_sum -= nums[lt]
                res = min(res, rt-lt+1) # 更新结果
                lt += 1
            rt += 1
        return 0 if res > len(nums) else res