# -*- coding: utf-8 -*-



class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        sz = len(s)
        for i in range(sz):
            # 每个字母本身是一个回文子串
            res += 1

            # 当前字母是奇数长度回文子串的中点
            lt, rt = i - 1, i + 1
            while lt >= 0 and rt < sz and s[lt] == s[rt]:
                res += 1
                lt -= 1
                rt += 1

            # 当前字母是偶数长度回文子串的中点
            lt, rt = i - 1, i
            while lt >= 0 and rt < sz and s[lt] == s[rt]:
                res += 1
                lt -= 1
                rt += 1

        return res

# 动态规划，没有上面的快，dp存储空间还可以优化，因为只用到了上一行，可以做成2行存储，交替更新
class Solution:
    def countSubstrings(self, s: str) -> int:
        sz = len(s)
        res = 0
        dp = [[0 for i in range(sz)] for i in range(sz)]
        # 即每次遍历以当前元素作为回文串最后一个值
        for i in range(sz):
            j = i
            while j>=0:
                if s[j]==s[i] and (i-j<2 or dp[j+1][i-1]):
                    dp[j][i] = 1
                    res += 1
                j -= 1
        return res
