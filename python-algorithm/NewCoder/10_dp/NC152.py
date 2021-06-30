#--coding:utf-8--

class Solution:
    def divideNumber(self , n , k ):
        # write code here
        dp = [[0]*(k+1) for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1,n+1):
            for j in range(1,k+1):
                if i-j >= 0:
                    # 两种情况，用i-1个数划分成j-1份 ； 用i-j个数划分成j份
                    dp[i][j] = dp[i-1][j-1] + dp[i-j][j]
        return dp[n][k]


# 回溯会超时
class Solution1:
    def divideNumber(self , n , k ):
        # write code here
        self.res = 0
        self.r_c = []
        def dfs(idx, cnt, num, tmp):
            if cnt == 0:
                if num == 0:
                    self.res += 1
                    self.r_c.append(tmp[:])
                return
            for i in range(idx, num+1):
                tmp.append(i)
                dfs(i, cnt-1, num-i, tmp)
                tmp.pop()
        dfs(1, k, n, [])
        return self.res

n, k = 7,  3
n, k = 200,  5
res = Solution1().divideNumber(n,k)
print(res)