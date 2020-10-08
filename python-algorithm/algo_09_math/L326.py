# -*- coding: utf-8 -*-
# @Time    : 2020/10/6 22:58
# @Author  : No Name

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        while n % 3 == 0:
            n = n//3
        return n == 1

# 进阶：不用循环/递归 该怎么做?