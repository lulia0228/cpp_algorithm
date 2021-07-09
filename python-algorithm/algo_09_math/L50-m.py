# -*- coding: utf-8 -*-

class Solution:
    def myPow(self, x: float, n: int) -> float:
        flag = 0
        m = n
        if n<0:
            m = -n
            flag = 1
        ans = 1
        while m:
            if m&1:
                ans *= x
            x *= x
            m //= 2
        return 1.0/ans if flag else ans

