#--coding:utf-8--

# dp[0][K] = 0, dp[N][1] = N, dp[N][K] = min(max(dp[i-1][K-1], dp[N-i][K])) + 1

class Solution:
    def solve(self , n , k ):
        # write code here
        if n<1 or k<1: return 0
        if k==1: return n
        dp = [[0]*(k+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][1] = i
        for i in range(1, n+1):
            for j in range(2,k+1):
                min_ = float("inf")
                for c in range(1,i+1):
                    min_ = min(min_, max(dp[c-1][j-1], dp[i-c][j]))
                dp[i][j] = min_ + 1
        return dp[n][k]

n,k = 1000000,1000000
res = Solution().solve(n, k)
print(res) #