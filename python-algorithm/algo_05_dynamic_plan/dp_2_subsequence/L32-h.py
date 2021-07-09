#--coding:utf-8--

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        sz = len(s)
        dp = [0]*(len(s))
        ans = 0
        for i in range(1,sz):
            if s[i] == ")":
                if s[i-1] == "(":
                    dp[i] = (dp[i-2] if i>1 else 0) + 2
                elif s[i-1] == ")":
                    last_match = i-dp[i-1]-1
                    if last_match>=0 and s[last_match]=="(":
                        dp[i] = (dp[last_match-1] if last_match>=1 else 0) + dp[i-1]+2
                ans = max(ans, dp[i])
        return ans