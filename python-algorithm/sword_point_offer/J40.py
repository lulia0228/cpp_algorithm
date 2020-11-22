# -*- coding: utf-8 -*-
# 未完成：用python 自己手写一个堆

import  heapq
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        res = []
        if k == 0:
            return res
        heaptree = []
        # heapq.heapify(heaptree) # 可要可不要，是让列表转化为堆
        for i in arr:
            print(len(heaptree))
            if len(heaptree) < k:
                heapq.heappush(heaptree,-i)
            else:
                if -i > heaptree[0]:
                    heapq.heappop(heaptree)
                    heapq.heappush(heaptree,-i)
        while heaptree:
            res.append(-heapq.heappop(heaptree))
        return res