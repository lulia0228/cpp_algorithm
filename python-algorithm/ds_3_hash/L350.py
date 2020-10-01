# -*- coding: utf-8 -*-
# @Time    : 2020/10/1 21:13
# @Author  : Heng Li
# @File    : L350.py
# @Software: PyCharm

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        d1, d2 = {}, {}
        for i in nums1:
            if i not in d1:
                d1[i] = 1
            else:
                d1[i] += 1
        for i in nums2:
            if i in d1:
                if i not in d2:
                    d2[i] = 1
                else:
                    d2[i] += 1
        for k,v in d2.items():
            for j in range(min(d1[k], v)):
                res.append(k)
        return res