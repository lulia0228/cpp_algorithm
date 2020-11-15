# -*- coding: utf-8 -*-

# 斐波拉契数列
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        a,b = 0,1
        c = 0
        for i in range(2, n+1):
            c = a+b
            a = b
            b = c
        return c%1000000007

# 青蛙跳台阶
class Solution:
    def numWays(self, n: int) -> int:
        if n == 0: return 1
        if n == 1: return 1
        a,b = 1,1
        for i in range(2, n+1):
            a, b = a+b, a
        return a%1000000007