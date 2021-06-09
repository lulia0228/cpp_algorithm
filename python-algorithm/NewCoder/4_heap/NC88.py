# -*- coding:utf-8 -*-

# 借助快排的partition,牛客这道题要求借助快排的思路

class Solution:
    def findKth(self, a, n, K):
        # write code here
        pos = 0
        low, high = 0, n - 1
        # 用二分法找分界点piov
        while low <= high:
            pos = self.partition(a, low, high)
            if pos == n - K:
                break
            elif pos < n - K:
                low = pos + 1
            else:
                high = pos - 1
        return a[pos]

    def partition(self, a, low, high):
        # 从小到大 排的过程
        piov = a[low]
        while high > low:
            # 从后向前找到第一个＞piov的值
            while high > low and a[high] >= piov:
                high -= 1
            a[low] = a[high]
            # 从前向后找到第一个＜piov的值
            while high > low and a[low] <= piov:
                low += 1
            a[high] = a[low]
        a[low] = piov
        return low



class Solution1:
    def findKth(self, a, n, K):
        # write code here
        pos = 0
        low, high = 0, n - 1
        while low <= high:
            pos = self.partition(a, low, high)
            if pos == K - 1:
                break
            elif pos < K - 1:
                low = pos + 1
            else:
                high = pos - 1
        return a[pos]

    def partition(self, a, low, high):
        # 从大到小排的过程
        piov = a[low]
        while high > low:
            # 从后向前找到第一个＞piov的值
            while high > low and a[high] <= piov:
                high -= 1
            a[low] = a[high]
            # 从前向后找到第一个＜piov的值
            while high > low and a[low] >= piov:
                low += 1
            a[high] = a[low]
        a[low] = piov
        return low

# 堆排序
import heapq
class Solution2:
    def findKth(self, a, n, K):
        # write code here
        my_heap = []
        for item in a:
            if len(my_heap)<K:
                heapq.heappush(my_heap, item)
            else:
                if item > my_heap[0]:
                    heapq.heappop(my_heap)
                    heapq.heappush(my_heap, item)
        return my_heap[0]