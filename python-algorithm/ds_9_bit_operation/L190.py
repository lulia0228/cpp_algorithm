# -*- coding: utf-8 -*-
# @Time    : 2020/10/7 11:18
# @Author  : No Name

class Solution:
    def reverseBits(self, n: int) -> int:
        ref = 1
        res = 0
        for i in range(32):
            pop = n&ref
            # res << 1必须加括号
            res = (res << 1) + pop
            # res += pop<<(31-i)
            n =  n >> 1
        return res