# -*- coding: utf-8 -*-
class Solution:
    def myPow(self, x: float, n: int) -> float:
        m = abs(n)
        res = 1.0
        while m:
            if m%2 == 1:
                res *= x
            x *= x
            m //= 2
        return 1.0/res if n<0 else res
