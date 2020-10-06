# -*- coding: utf-8 -*-
# @Time    : 2020/10/6 13:56
# @Author  : No Name

class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        if n > 0 :
            m = n
        else:
            m = -n
        x_con = x
        while m :
            if m%2 == 1:
                res *= x_con
            x_con *= x_con
            m = m // 2
        return res if n>0 else 1/res