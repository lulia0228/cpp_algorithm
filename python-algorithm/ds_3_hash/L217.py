# -*- coding: utf-8 -*-
# @Time    : 2020/10/1 20:13
# @Author  : Heng Li
# @File    : L217.py
# @Software: PyCharm

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for num in nums:
            if num in s:
                return True
            s.add(num)
        return False