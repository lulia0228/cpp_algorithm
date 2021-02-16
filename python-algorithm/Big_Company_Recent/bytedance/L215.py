# -*- coding: utf-8 -*-
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        my_hp = []
        for i in range(len(nums)):
            if len(my_hp) < k:
                heapq.heappush(my_hp, nums[i])
            else:
                if my_hp[0] < nums[i]:
                    heapq.heappop(my_hp)
                    heapq.heappush(my_hp, nums[i])
        return my_hp[0]

