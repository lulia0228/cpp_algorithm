# -*- coding: utf-8 -*-
# @Time    : 2020/10/6 19:28
# @Author  : No Name
# n的阶乘中，可以分解成约数5的个数 决定最终末尾的0的个数
# 最终 5 的个数就是 n / 5 + n / 25 + n / 125 ...

# 这是一道数学题，需要细致分析

class Solution:
    def trailingZeroes(self, n: int) -> int:
        cnt = 0
        while n:
            cnt += n//5
            n = n//5
        return cnt