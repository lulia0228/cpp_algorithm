# -*- coding: utf-8 -*-

# 原题目等价于找到一个包含0的数目不超过1、包含1的数目最多的子串。

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        lt = rt = 0
        res = 0
        cnt_zero = 0
        sz = len(nums)
        contain0 = False
        while rt < sz:
            if nums[rt] == 0:
                cnt_zero += 1
            while cnt_zero > 1:
                if nums[lt] == 0:
                    cnt_zero -= 1
                lt += 1
            res = max(res, rt-lt+1-cnt_zero)
            if cnt_zero != 0:
                contain0 = True
            rt += 1
        if contain0:
            return res
        else:
            return res-1

