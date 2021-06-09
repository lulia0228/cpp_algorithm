# -*- coding:utf-8 -*-

import heapq
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        sz = len(tinput)
        if k > sz or k < 1: return []
        res = []
        my_heap = []
        for n in tinput:
            if len(my_heap) < k:
                heapq.heappush(my_heap, [-n, n])
            else:
                if -n > my_heap[0][0]:
                    heapq.heappop(my_heap)
                    heapq.heappush(my_heap, [-n, n])
        while my_heap:
            res.append(heapq.heappop(my_heap)[1])
        return res[::-1]