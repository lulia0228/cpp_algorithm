# -*- coding: utf-8 -*-

# 同leetcode 91
class Solution:
    def translateNum(self, num: int) -> int:
        nums = str(num)
        dp = [0]*(len(nums)+1)
        dp[0] = dp[1] = 1
        for i in range(2, len(nums)+1):
            if 10 <= int(nums[i-2:i])  <= 25:
                dp[i] = dp[i-2] + dp[i-1]
            else:
                dp[i] = dp[i-1]
        return dp[len(nums)]

