#--coding:utf-8--
import heapq


# python默认是小顶堆
class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        if k == 0: return []
        my_heap = []
        for item in arr:
            if len(my_heap) < k:
                heapq.heappush(my_heap, -item)
            else:
                if -item > my_heap[0]:
                    heapq.heappop(my_heap)
                    heapq.heappush(my_heap, -item)
        res = []
        while len(my_heap):
            res.append(-heapq.heappop(my_heap))
        return res
