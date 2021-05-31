#--coding:utf-8--
class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        p3, p5, p7 = 0, 0, 0
        dp =  [0]*k
        dp[0]=1
        for i in range(1,k):
            dp[i]=min(dp[p3]*3, min(dp[p5]*5, dp[p7]*7))
            if dp[i]==dp[p3]*3: p3 += 1
            if dp[i]==dp[p5]*5: p5 += 1
            if dp[i]==dp[p7]*7: p7 += 1
        return dp[k-1];

