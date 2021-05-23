# -*- coding: utf-8 -*-
'''
1 定义状态
dp[i]：到nums[i]为止的最长递增子序列长度
count[i]：到nums[i]为止的最长递增子序列个数
2 初始化状态
dp = [1] * n：代表最长递增子序列的长度至少为1
count = [1] * n：代表最长递增子序列的个数至少为1
3 状态转移
如果dp[j] + 1 > dp[i]，说明最长递增子序列的长度增加了，dp[i] = dp[j] + 1，长度增加，数量不变 count[i] = count[j]
如果dp[j] + 1 == dp[i]，说明最长递增子序列的长度并没有增加，但是出现了长度一样的情况，数量增加 count[i] += count[j]
'''

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 1

        dp = [1] * n
        count = [1] * n
        max_length = 0
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[j] + 1 == dp[i]:
                        count[i] += count[j]
            max_length = max(max_length, dp[i])

        res = 0
        for i in range(n):
            if dp[i] == max_length:
                res += count[i]
        return res

