# -*- coding: utf-8 -*-

# 同leetcode 50
class Solution:
    def myPow(self, x: float, n: int) -> float:
        m = n
        if n < 0:
            m = -n
        res = 1.0
        while m:
            if m&1 == 1:
                res *= x
            x *= x
            m = m//2
        return res if n>0 else 1.0/res