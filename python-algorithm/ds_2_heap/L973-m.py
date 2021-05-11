#--coding:utf-8--

import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        my_heap = []
        for p in points:
            distance = pow(p[0], 2) + pow(p[1], 2)
            if len(my_heap) < k:
                heapq.heappush(my_heap, [-distance]+p)
            else:
                if -distance > my_heap[0][0]:
                    heapq.heappop(my_heap)
                    heapq.heappush(my_heap, [-distance] + p)
        res = []
        while len(my_heap):
            res.append(heapq.heappop(my_heap)[1:])
        return res