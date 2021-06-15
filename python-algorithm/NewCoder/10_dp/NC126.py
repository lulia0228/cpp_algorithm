#--coding:utf-8--

# 同lc 322 零钱兑换
class Solution:
    def minMoney(self , arr , aim ):
        # write code here
        dp = [aim+1]*(aim+1)
        dp[0] = 0
        for i in range(1, aim+1):
            for coin in arr:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        return -1 if dp[aim] == aim+1 else dp[aim]