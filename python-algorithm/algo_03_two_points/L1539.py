# -*- coding: utf-8 -*-
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        p1 = 0
        p2 = 1
        cnt = 0
        while cnt < k and p1 < len(arr):
            if arr[p1] != p2:
                cnt += arr[p1]-p2
                p2 += arr[p1]-p2
                if cnt >= k:
                    return p2-(cnt-k)-1
            else:
                p1 += 1
                p2 += 1
        if cnt < k:
            return p2 +(k-cnt)-1