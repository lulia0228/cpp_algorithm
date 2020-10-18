# -*- coding: utf-8 -*-


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        while n % 3 == 0:
            n = n//3
        return n == 1

# 进阶：不用循环/递归 该怎么做?