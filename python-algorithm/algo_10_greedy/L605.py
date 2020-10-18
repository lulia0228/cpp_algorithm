# -*- coding: utf-8 -*-


# 一次遍历，同时看前后是否为0
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        sz = len(flowerbed)
        cnt = 0
        for i in range(sz):
            if flowerbed[i] == 1:
                continue
            pre = (0 if i==0 else flowerbed[i-1])
            nxt = (0 if i==sz-1 else flowerbed[i+1])
            if pre==0 and nxt==0:
                cnt += 1
                flowerbed[i] = 1 # 容易漏掉
        return cnt >= n
