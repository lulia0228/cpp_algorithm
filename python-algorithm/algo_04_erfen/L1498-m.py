# -*- coding: utf-8 -*-

# 排序+二分+计算排列数

# 固定最小值，然后二分寻找数组最大值
# vmin≤vmax≤target−vmin

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        P = 10 ** 9 + 7
        f = [1] + [0] * (n - 1)
        for i in range(1, n):
            f[i] = f[i - 1] * 2 % P

        nums.sort()
        ans = 0
        for i, num in enumerate(nums):
            if nums[i] * 2 > target:
                break
            maxValue = target - nums[i]
            pos = bisect.bisect_right(nums, maxValue) - 1
            # pos-i是原数组第一个小于等于目标值的索引
            contribute = f[pos - i] if pos >= i else 0
            ans += contribute

        return ans % P
