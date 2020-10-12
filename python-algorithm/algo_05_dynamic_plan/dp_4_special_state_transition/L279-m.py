#--coding:utf-8--
'''
@Time   : 2020/10/12
@Author : No Name
'''

# 动态规划：可以看作是完全背包问题
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [i for i in range(n+1)]
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+1):
            for j in range(1, int(sqrt(i))+1):
                dp[i] = min(dp[i], dp[i-j*j]+1)
        return dp[n]

# 宽搜
class Solution:
    def numSquares(self, n: int) -> int:
        visited = [0] * (n + 1)
        que = []
        que.append(0)
        level = 0
        while que != []:
            level += 1
            for i in range(len(que)):
                cur = que.pop(0)
                if cur == n:
                    return level - 1
                for j in range(1, int(sqrt(n)) + 1):
                    tmp = cur + j*j
                    if tmp <= n and not visited[tmp]:
                        que.append(tmp)
                        visited[tmp] = 1
