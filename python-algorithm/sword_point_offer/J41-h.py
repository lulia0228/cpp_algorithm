# -*- coding: utf-8 -*-

# 同leetcode295
import heapq
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        # python heapq库默认小顶堆，用负数才能达到模拟大根堆的效果
        if self.max_heap == [] or self.max_heap[0][0] < -num:
            heapq.heappush(self.max_heap, (-num, num))
        else:
            heapq.heappush(self.min_heap, num)
        if len(self.max_heap) == len(self.min_heap) + 2:
            tmp = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, tmp[1])
        if len(self.max_heap) == len(self.min_heap) - 1:
            tmp = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, (-tmp, tmp))

    def findMedian(self) -> float:
        return self.max_heap[0][1] if len(self.max_heap) != len(self.min_heap) \
            else (self.max_heap[0][1] + self.min_heap[0]) / 2.0



        # Your MedianFinder object will be instantiated and called as such:
        # obj = MedianFinder()
        # obj.addNum(num)
        # param_2 = obj.findMedian()