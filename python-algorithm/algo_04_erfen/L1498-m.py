# -*- coding: utf-8 -*-

# 排序+二分+计算排列数
# 固定最小值，然后二分寻找数组最大值
# vmin≤vmax≤target−vmin
import bisect
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        P = 10 ** 9 + 7
        nums.sort()
        ans = 0
        for i, num in enumerate(nums):
            if nums[i] * 2 > target:
                break
            maxValue = target - nums[i]
            # pos = bisect.bisect_right(nums, maxValue) - 1
            pos = self.find_last_(nums, i, maxValue)
            # pos是原数组最后一个小于等于目标值的索引
            contribute = 1<<(pos - i) if pos >= i else 0
            ans += contribute
        return ans % P

    def find_last_(self, nums, start, target):
        lt, rt = start, len(nums)-1
        while lt<rt:
            mid = lt+(rt-lt+1)//2
            if nums[mid]>target:
                rt = mid-1
            else:
                lt = mid
        return lt

# 双指针
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        if nums[0] * 2 > target:
            return 0

        left = 0
        right = len(nums) - 1
        res = 0
        while left <= right:
            if nums[left] + nums[right] <= target:
                # [min n1 n2 n3 ... max] 其中[n1 n2 max]的所有子集(包括空)
                # 共2**(right-left)个均可以与n1组成满足要求的子序列
                res += 1 << (right - left)  # 位运算速度更快
                left += 1
            else:
                right -= 1
        return res % (10 ** 9 + 7)