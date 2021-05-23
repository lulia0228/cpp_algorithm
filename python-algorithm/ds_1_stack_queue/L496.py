# -*- coding: utf-8 -*-
# 单调栈
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        r_d = {}
        stk = []
        for i in range(len(nums2)):
            while stk and nums2[stk[-1]] < nums2[i]:
                t_idx = stk.pop()
                r_d[nums2[t_idx]] = nums2[i]
            stk.append(i)
        res = [-1]*len(nums1)
        for idx,n in enumerate(nums1):
            if n in r_d:
                res[idx] = r_d[n]
        return res