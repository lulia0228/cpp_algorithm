# -*- coding: utf-8 -*-

# 动态规划O(n*n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sz = len(nums)
        dp = [1]*sz  # dp[i]表示以nums[i]作为结尾的最长上升子序列
        max_len = 1
        for i in range(1, sz):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            max_len = max(max_len, dp[i])
        return max_len


# 二分法；很难想到
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        (1)新建数组，record[i]最终表示的是长度为i+1的递增子序列中尾数最小的值；因此record是递增的
        (2)在遍历时通过二分法确定元素应该被放到record中的具体位置，因此时间复杂度是N*logN
        '''
        maxL = 0
        record = [0]*(len(nums))
        for nu in nums:
            lt, rt = 0, maxL
            while lt<rt:
                mid = lt + (rt-lt)//2
                if record[mid]<nu:
                    lt = mid + 1
                else:
                    rt = mid
            record[lt] = nu
            if lt == maxL:
                maxL += 1
        return maxL