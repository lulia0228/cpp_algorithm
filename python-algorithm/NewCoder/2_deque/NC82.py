

# 双端队列；单调队列(不增)
# -*- coding:utf-8 -*-
import collections
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        res = []
        if size == 0 or size > len(num):
            return res
        sz = len(num)
        que = collections.deque()
        for w_start, w_end in zip(range(1 - size, sz - size + 1), range(sz)):
            if w_start > 0 and num[w_start - 1] == que[0]:
                que.popleft()
            # 保证窗口内是单调不增的
            while que and que[-1] < num[w_end]:
                que.pop()
            que.append(num[w_end])
            if w_start >= 0:
                res.append(que[0])
        return res



# 堆
import heapq
class Solution1:
    def maxInWindows(self, num, size):
        # write code here
        sz = len(num)
        res = []
        if  size > sz or size < 1: return res
        my_heap = [[-val, idx] for idx,val in enumerate(num[:size])]
        heapq.heapify(my_heap)
        res.append(-my_heap[0][0])
        for i in range(sz-size):
            heapq.heappush(my_heap, [-num[i+size], i+size])
            # 下面的条件最重要
            while my_heap[0][1] <= i:
                heapq.heappop(my_heap)
            res.append(-my_heap[0][0])

        return res