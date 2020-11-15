# -*- coding: utf-8 -*-

# /剑指 Offer 21. 调整数组顺序使奇数位于偶数前面

class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        lt, rt = 0, len(nums)-1
        n_nums = nums
        while lt < rt:
            while lt < len(nums) and n_nums[lt]&1 == 1:
                lt += 1
            while rt >= 0 and n_nums[rt]&1 == 0:
                rt -= 1
            if lt < rt :
                n_nums[lt], n_nums[rt] = n_nums[rt], n_nums[lt]
                lt += 1
                rt -= 1
        return n_nums