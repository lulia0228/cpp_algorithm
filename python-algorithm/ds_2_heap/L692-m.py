# -*- coding: utf-8 -*-

# 因为python heapq不支持自定义比较函数，
# 这道题需要多个条件比较堆中元素，因此放弃使用堆，直接排序了

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = {}
        for i in words:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        new_d = sorted(d.items(), key=lambda x:(-x[1], x[0]))
        res = [new_d[i][0] for i in range(k)]
        return res