# -*- coding: utf-8 -*-

class Solution:
    def longestPalindrome(self, s: str) -> str:
        sz = len(s)
        max_len, max_len_start = 1, 0
        dp = [[0]*sz for _ in range(sz)]
        for i in range(sz):
            j = i
            while j >= 0 :
                if s[i] == s[j]  and (i-j < 2 or dp[j+1][i-1] ):
                    dp[j][i] = 1
                    if i-j+1 > max_len:
                        max_len_start = j
                        max_len = max(max_len, i-j+1)
                j -= 1
        return s[max_len_start:max_len_start+max_len]

# 中心扩展 更快
class Solution:
    def longestPalindrome(self, s: str) -> str:
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
        return s[start: start+max_len]


# 马拉车算法
# ......