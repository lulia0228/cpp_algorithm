#
# the medians
# @param operations int整型二维数组 ops
# @return double浮点型一维数组
#

import heapq
class Solution:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def flowmedian(self, operations):
        # write code here
        res = []
        for op in operations:
            if op[0] == 1:
                if not self.max_heap or -op[1] > self.max_heap[0][0]:
                    heapq.heappush(self.max_heap, [-op[1], op[1]])
                else:
                    heapq.heappush(self.min_heap, op[1])
                # 即维持大顶堆中的数据量要么和小顶堆相等，要么多1
                if len(self.max_heap) == len(self.min_heap) + 2:
                    tmp = heapq.heappop(self.max_heap)
                    heapq.heappush(self.min_heap, tmp[1])
                if len(self.max_heap) == len(self.min_heap) - 1:
                    tmp = heapq.heappop(self.min_heap)
                    heapq.heappush(self.max_heap, [-tmp, tmp])
            else:
                if len(self.max_heap) == 0:
                    res.append(-1)
                else:
                    if len(self.max_heap) != len(self.min_heap):
                        res.append(self.max_heap[0][1])
                    else:
                        res.append((self.max_heap[0][1] + self.min_heap[0]) / 2.0)
        return res


