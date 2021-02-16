# -*- coding: utf-8 -*-

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sz = len(nums)
        if sz == 0: return 0
        s = set(nums)
        max_len = 1
        for i in range(sz):
            tmp_len = 1
            if nums[i]-1 not in s:
                tmp_val = nums[i] + 1
                while tmp_val in s:
                    tmp_len += 1
                    s.remove(tmp_val)
                    tmp_val += 1
            max_len = max(max_len, tmp_len)
        return max_len

