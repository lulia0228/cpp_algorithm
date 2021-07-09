# -*- coding: utf-8 -*-
class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n:
            # n&(n-1)可将n最右边的二进制位1变成0
            n = n&(n-1)
            cnt += 1
        return cnt