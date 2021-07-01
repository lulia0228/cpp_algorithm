# -*- coding: utf-8 -*-


# python堆模块heapq是小顶堆，索引0处为最小值
# 堆底层数据结构，时空复杂度要搞清楚

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heaptree = []
        for i in nums:
            if len(heaptree) < k:
                heapq.heappush(heaptree,i)
            else:
                if i > heaptree[0]:
                    heapq.heappop(heaptree)
                    heapq.heappush(heaptree,i)
        return heaptree[0]

# 还有就是写快排了
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            # 利用快排思想找中点
            mid = self.find_pivot(nums, low, high)
            if mid == k - 1:
                return nums[mid]
            elif mid < k - 1:
                low = mid + 1
            else:
                high = mid - 1

    def find_pivot(self, nums, lt, rt):
        pivot = nums[lt]
        while lt < rt:
            while lt < rt and nums[rt] <= pivot:
                rt -= 1
            nums[lt] = nums[rt]
            while lt < rt and nums[lt] >= pivot:
                lt += 1
            nums[rt] = nums[lt]
        nums[lt] = pivot
        return lt


