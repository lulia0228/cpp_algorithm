# -*- coding: utf-8 -*-


# 这道题可以认为给定的nums 是wordDict ，里面的单词可使用0次或者无限次
# 约束则是按照上面的使用规则形成 s
# 目标是：判断是否可以组成s。

# 这道题不太好判断到底是外层循环约束，还是内层循环约束

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        # dp[i]表示s[:i]能否拆分成字典中的单词
        dp = [0]*(n+1)
        dp[0] = 1
        # 外层遍历约束
        for i in range(1, n+1):
            # 内层遍历nums
            for word in wordDict:
                if s[i-len(word):i] == word  and dp[i-len(word)]:
                    dp[i] = 1
        return dp[n] == 1