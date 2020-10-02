# -*- coding: utf-8 -*-
# @Time    : 2020/10/2 12:38
# @Author  : Heng Li
# @File    : L215-m.py
# @Software: PyCharm

# python堆模块heapq是小顶堆，索引0处为最小值
# 堆底层数据结构，时空复杂度要搞清楚

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heaptree = []
        for i in nums:
            if len(heaptree) < k:
                heapq.heappush(heaptree,i)
            else:
                if i > heaptree[0]:
                    heapq.heappop(heaptree)
                    heapq.heappush(heaptree,i)
        return heaptree[0]

# 还有就是写快排了