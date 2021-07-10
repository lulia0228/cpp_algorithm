# -*- coding: utf-8 -*-
from typing import  *

# 因为python heapq默认的是小根堆，而这里又要求频率相同的话，选择字典序小的数字
# 所以自定义入堆的元素为类对象，借助__lt__方法实现类对象的比较
class Word:
    def __init__(self, w, f):
        self.w = w
        self.f = f

    def __lt__(self, other):
        # 即频次小的会在堆顶；如果频次相同，字典序靠后(python字符串比较较大的一个)的会在堆顶
        if self.f < other.f or (self.f == other.f and self.w > other.w):
            return True
        else:
            return False

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_freq = [Word(w, f) for w, f in collections.Counter(words).items()]
        heap = []
        for word in word_freq:
            heapq.heappush(heap, word)
            if len(heap) > k:
                heapq.heappop(heap)
            # 也可以下面这样写
            '''if len(heap)<k:
                heapq.heappush(heap, word)
            else:
                if heap[0]<word:
                    heapq.heappop(heap)
                    heapq.heappush(heap, word)'''
        ans = [""] * k
        for i in range(k - 1, -1, -1):
            ans[i] = heapq.heappop(heap).w
        return ans

