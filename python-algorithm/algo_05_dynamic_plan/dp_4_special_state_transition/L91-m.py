#--coding:utf-8--

class Solution:
    def numDecodings(self, s: str) -> int:
        sz = len(s)
        dp = [0] * (sz + 1)
        dp[0] = 1
        dp[1] = 1 if s[0] != "0" else 0
        for i in range(2, sz + 1):
            if s[i - 1] == "0":
                if 10 <= int(s[i - 2:i]) <= 20:
                    dp[i] = dp[i - 2]
            else:
                if 10 < int(s[i - 2:i]) <= 26:
                    dp[i] = dp[i - 1] + dp[i - 2]
                else:
                    dp[i] = dp[i - 1]
        return dp[sz]





