#--coding:utf-8--
class Solution:
    def longestWord(self, words: List[str]) -> str:
        res = []
        sz = len(words)
        res_str, max_len = "", 0
        for i in range(sz):
            if self.canMade(words, i):
                if len(words[i]) > max_len:
                    max_len = len(words[i])
                    res_str = words[i]
                elif len(words[i]) == max_len:
                    if words[i] < res_str or res_str == "":
                        res_str = words[i]
        return res_str

    def canMade(self, words, idx):
        sz = len(words[idx])
        dp = [False] * (sz + 1)
        dp[0] = True
        for i in range(sz):
            for j in range(len(words)):
                if j == idx: continue
                tmp_sz = len(words[j])
                if i >= tmp_sz - 1 and words[idx][i + 1 - tmp_sz:i + 1] == words[j]:
                    if dp[i + 1 - tmp_sz]:  # 必须的
                        dp[i + 1] = dp[i + 1 - tmp_sz]
        return dp[sz]
