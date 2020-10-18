# -*- coding: utf-8 -*-


import  heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        my_heap = []
        for key,val in d.items():
            if len(my_heap) < k :
                heapq.heappush(my_heap, (val, key))
            else:
                if my_heap[0][0]<val:
                    heapq.heappop(my_heap)
                    heapq.heappush(my_heap, (val, key))
        # print(my_heap)
        res = []
        while my_heap!= []:
            res.append(heapq.heappop(my_heap)[1])
        return res

