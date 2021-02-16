# -*- coding: utf-8 -*-
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        if n < 3:
            return n
        for i in range(2, n+1):
            c = a + b
            a, b = b, c
        return c