#--coding:utf-8--
class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        sz = len(sentence)
        dp = [0]*(sz+1)
        for i in range(sz):
            for word in dictionary:
                tmp_sz = len(word)
                if i>=tmp_sz-1 and sentence[i+1-tmp_sz:i+1]==word:
                    dp[i+1] = max(dp[i+1-tmp_sz]+tmp_sz, dp[i+1])
                else:
                    dp[i+1] = max(dp[i+1], dp[i])
        return sz - dp[sz]