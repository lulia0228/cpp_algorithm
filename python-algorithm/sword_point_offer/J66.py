# -*- coding: utf-8 -*-

# 同leetcode 题
# 为了保证空间常数复杂度；存放返回数组的res不计算成空间复杂度
class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        res = [1]*len(a)
        for i in range(1, len(a)):
            res[i] = res[i-1]*a[i-1]
        tmp = 1
        for i in range(len(a)-1,-1,-1):
            res[i] *= tmp
            tmp *= a[i]
        return res