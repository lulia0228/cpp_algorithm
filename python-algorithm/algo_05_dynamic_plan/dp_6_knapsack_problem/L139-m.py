# -*- coding: utf-8 -*-


# 这道题可以认为给定的nums 是wordDict ，里面的单词可使用0次或者无限次
# 约束则是按照上面的使用规则形成 s
# 目标是：判断是否可以组成s。

# 这道题不太好判断到底是外层循环约束，还是内层循环约束

# 1 DP 完全背包
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
