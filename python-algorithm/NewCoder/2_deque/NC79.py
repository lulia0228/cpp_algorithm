# -*- coding:utf-8 -*-

class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index == 0: return 0
        p1, p2, p3 = 0, 0, 0
        dp = [1 for _ in range(index)]
        for i in range(1, index):
            n2, n3, n5 = dp[p1] * 2, dp[p2] * 3, dp[p3] * 5
            tmp = min(n2, n3, n5)
            if tmp == n2: p1 += 1
            if tmp == n3: p2 += 1
            if tmp == n5: p3 += 1
            dp[i] = tmp
        return dp[-1]


# 堆
import heapq
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index==0: return 0
        factors = [2, 3, 5]
        seen = {1}
        heap = [1]

        for i in range(index - 1):
            curr = heapq.heappop(heap)
            for factor in factors:
                nxt = curr * factor
                if nxt not in seen:
                    seen.add(nxt)
                    heapq.heappush(heap, nxt)

        return heapq.heappop(heap)