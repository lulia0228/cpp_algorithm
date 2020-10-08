# -*- coding: utf-8 -*-
# @Time    : 2020/10/7 12:36
# @Author  : No Name

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ret = x^y
        cnt = 0
        while ret:
            cnt += 1
            ret = ret&(ret-1)
        return cnt