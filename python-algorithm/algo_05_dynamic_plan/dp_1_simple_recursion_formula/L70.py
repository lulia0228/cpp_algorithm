# -*- coding: utf-8 -*-
# @Time    : 2020/10/8 10:01
# @Author  : No Name

class Solution:
    def climbStairs(self, n: int) -> int:
        if n<3:
            return n
        a = 1
        b = 2
        c = 0
        for i in range(3, n+1):
            c = a+b
            a = b
            b = c
        return c


# 斐波拉契数列，生成器写法
# 0 1 1 2 3 5 8 13 21……生成器斐波那契

def fb():
    x,y = 0, 1
    while True:
        n=x+y
        x=y
        y=n
        yield n

fb=fb()
print(0)
for i in range(20):
    print(next(fb))