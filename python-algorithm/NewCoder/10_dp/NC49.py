#--coding:utf-8--

# lc32

# dp[i]表示以s[i]作为结尾的最长有效括号的长度
class Solution:
    def longestValidParentheses(self , s ):
        # write code here
        dp = [0]*len(s)
        res = 0
        for i in range(1, len(s)):
            if s[i] == ")" and s[i-1] == "(":
                dp[i] = (dp[i-2] if i>=2 else 0) + 2
            elif s[i] == ")" and s[i-1] == ")":
                if i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '(':
                    dp[i] = dp[i-1] + 2 + (dp[i-dp[i-1]-2] if i-dp[i-1]-2>=0  else 0)
            res = max(res, dp[i])
        return res