#--coding:utf-8--

# 贪心
class Solution:
    def Jump(self , n , A ):
        # write code here
        cnt = 0
        far, end = 0, 0
        for i,num in enumerate(A):
            far = max(far, i+num)
            if end >= n:
                break
            if end == i:
                end = far
                cnt += 1
        return cnt

class Solution1:
    def Jump(self , n , A ):
        # write code here
        dp = [n]*n
        dp[0] = 0
        for i in range(1, n):
            for j in range(i,-1,-1):
                if A[j]>=i-j:
                    dp[i] = min(dp[j]+1,dp[i])
        return dp[n-1]

arr = []
res = Solution().Jump(len(arr), arr)