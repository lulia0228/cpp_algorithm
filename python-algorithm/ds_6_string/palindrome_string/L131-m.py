# -*- coding: utf-8 -*-

# 131 分割回文串
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        sz = len(s)
        dp = [[0 for i in range(sz)] for i in range(sz)]
        # 即每次遍历以当前元素作为回文串最后一个值
        for i in range(sz):
            j = i
            while j>=0:
                if s[j]==s[i] and (i-j<2 or dp[j+1][i-1]):
                    dp[j][i] = 1
                j -= 1
        res = []
        tmp = []
        self.dfs(s, 0, dp, tmp, res)
        return res

    def dfs(self, s, start, dp, tmp, res):
        if start==len(s):
            res.append(tmp[:])
        for j in range(start, len(s)):
            if dp[start][j]:
                tmp.append(s[start:j+1])
                self.dfs(s, j+1, dp, tmp, res)
                tmp.pop()