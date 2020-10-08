# -*- coding: utf-8 -*-
# @Time    : 2020/10/7 12:33
# @Author  : No Name

# a ^ b可以得到两数相加不进位的加法结果
# (a & b) << 1可以得到两数相加产生的进位
class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b:
            tmp = (a&b) << 1
            a = a^b
            b = tmp
        return a