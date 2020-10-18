# -*- coding: utf-8 -*-



# 动态规划
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0 for i in range(num+1)]
        for i in range(1, num+1):
            res[i] = res[i>>1] + (i&1);
        return res
