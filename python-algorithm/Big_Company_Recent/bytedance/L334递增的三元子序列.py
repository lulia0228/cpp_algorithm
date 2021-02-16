# -*- coding: utf-8 -*-


# 双指针吧
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        sz = len(nums)
        if sz < 3:
            return False
        small = mid = inf
        for i in range(sz):
            if nums[i] <= small:
                small = nums[i]
            elif nums[i] <= mid:
                mid = nums[i]
            else:
                return True
        return False
    # class Solution {


# 动态规划
class Solution1:
    def increasingTriplet(self, nums: List[int]) -> bool:
        sz = len(nums)
        dp = [1]*sz
        for i in range(sz) :
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
                if dp[i] >= 3:
                    return True
        return False