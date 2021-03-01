# -*- coding: utf-8 -*-

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def translateNum(self, num: int) -> int:
        sz = len(str(num))
        dp = [0]*(sz+1)
        dp[0] = dp[1] = 1
        for i in range(2, sz+1):
            if 10<=int(str(num)[i-2:i])<26:
                dp[i] = dp[i-1]+dp[i-2]
            else:
                dp[i] = dp[i-1]
        return dp[sz]
# leetcode submit region end(Prohibit modification and deletion)