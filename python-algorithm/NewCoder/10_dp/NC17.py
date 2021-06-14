# -*- coding: utf-8 -*-

class Solution:
    def getLongestPalindrome(self, A, n):
        # write code here
        res = 1
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n):
            j = i
            while j>=0:
                if A[j] == A[i] and (i-j<2 or dp[j+1][i-1]):
                    dp[j][i] = 1
                    res = max(res, i-j+1)
                j -= 1
        return res

class Solution:
    def getLongestPalindrome(self, s, n):
        # write code here
        if s == "":
            return ""
        start, max_len = 0, 1
        sz = len(s)
        for i in range(sz):
            # 当前字母是奇数长度回文子串的中点
            lt, rt = i - 1, i + 1
            while lt >= 0 and rt < sz and s[lt] == s[rt]:
                lt -= 1
                rt += 1
            if rt-lt-1 > max_len:
                start = lt+1
                max_len = rt-lt-1
            # 当前字母是偶数长度回文子串的中点
            lt, rt = i - 1, i
            while lt >= 0 and rt < sz and s[lt] == s[rt]:
                lt -= 1
                rt += 1
            if rt-lt-1 > max_len:
                start = lt+1
                max_len = rt-lt-1
        return max_len