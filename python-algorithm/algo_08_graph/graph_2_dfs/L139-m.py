# -*- coding: utf-8 -*-
# 1 DP
from typing import *
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        sz = len(s)
        dp = [False]*(sz+1)
        dp[0] = True
        for i in range(1, sz+1):
            for word in wordDict:
                if i-len(word)>=0 and s[i-len(word):i]==word and dp[i-len(word)]:
                    dp[i] = True
        return dp[sz]

# 2 DFS回溯
# 超时
class Solution1:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        res = []
        self.dfs(s, wordDict, 0, [], res)
        # print(res)
        return res != []

    def dfs(self, s, wordDict, idx, tmp, res):
        if idx==len(s):
            res.append(tmp[:])
            return
        for word in wordDict:
            if idx+len(word)>len(s) or s[idx:idx+len(word)] != word:
                continue
            tmp.append(word)
            self.dfs(s, wordDict, idx+len(word), tmp, res)
            tmp.pop()

s = "acaaaaabbbdbcccdcdaadcdccacbcccabbbbcdaaaaaadb"
wordDict = ["abbcbda","cbdaaa","b","dadaaad","dccbbbc","dccadd","ccbdbc","bbca","bacbcdd","a","bacb","cbc","adc","c","cbdbcad","cdbab","db","abbcdbd","bcb","bbdab","aa","bcadb","bacbcb","ca","dbdabdb","ccd","acbb","bdc","acbccd","d","cccdcda","dcbd","cbccacd","ac","cca","aaddc","dccac","ccdc","bbbbcda","ba","adbcadb","dca","abd","bdbb","ddadbad","badb","ab","aaaaa","acba","abbb"]
res = Solution1().wordBreak(s, wordDict)
print(res)
