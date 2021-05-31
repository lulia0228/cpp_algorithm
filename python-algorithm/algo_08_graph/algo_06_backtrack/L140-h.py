# -*- coding: utf-8 -*-

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        lenth = len(s)
        self.dfs(s, wordDict, 0, [], res)
        return res

    def dfs(self, s, wordDict, start, tmp, res):
        if start == len(s):
            res.append(" ".join(tmp))
            return
        for i in range(start, len(s)):
            tmp_str = s[start:i+1]
            if tmp_str in wordDict:
                tmp.append(tmp_str)
                # 是i+1,不是start+1
                self.dfs(s, wordDict, i+1, tmp, res)
                tmp.pop()

# 以下特殊案例超时
# s = "aaa...aaa"
# wordDict = ["a","aa","aaa", ..., "aaa...aaa"]

# 结合139的动态规划看看