# -*- coding: utf-8 -*-
# @Time    : 2020/10/1 21:06
# @Author  : Heng Li
# @File    : L349.py
# @Software: PyCharm

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = set(nums1)
        res = set()
        for i in nums2:
            # 把nums1存到s集合，判断i in s 比i in nums1快很多
            if i in s:
                res.add(i)
        return res