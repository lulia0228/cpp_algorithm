# -*- coding: utf-8 -*-
class Solution:
    def translateNum(self, num: int) -> int:
        num = str(num)
        sz = len(num)
        dp = [0]*(sz+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, sz+1):
            if 10<=int(num[i-2:i])<=25:
                dp[i] = dp[i-1]+dp[i-2]
            else:
                dp[i] = dp[i-1]
        return dp[sz]
