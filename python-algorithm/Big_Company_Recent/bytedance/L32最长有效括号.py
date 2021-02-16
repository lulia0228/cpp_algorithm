# -*- coding: utf-8 -*-
# 栈
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stk = []
        max_len = 0
        stk.append(-1) # 很关键，很巧妙
        for i in range(len(s)):
            if s[i] == "(":
                stk.append(i)
            else:
                stk.pop(-1)
                if stk == []:
                    stk.append(i)
                else:
                    max_len = max(max_len, i-stk[-1])
        return max_len

# 动态规划
# dp[i]表示以s[i-1]作为结尾的最长有效括号序列的长度
# 两种情况：
# （1）s[i] = ")" s[i-1] = "("
#   dp[i] = dp[i−2] + 2
# （2）s[i] = ")" s[i-1] = ")"  and s[i-dp[i-1]-1]=="("
#   dp[i] = dp[i−1] + dp[i−dp[i−1]−2] + 2

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        sz = len(s)
        dp = [0]*sz
        max_len = 0
        for i in range(1, sz):
            if s[i] == ')' and s[i-1] == '(':
                dp[i] = (dp[i-2] if i>=2 else 0) + 2
            elif s[i] == ')' and s[i-1] == ')':
                if i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '(':
                    dp[i] = dp[i-1] + (dp[i-dp[i-1]-2] if i-dp[i-1]>=2 else 0) + 2
            max_len = max(max_len, dp[i])
        return max_len

