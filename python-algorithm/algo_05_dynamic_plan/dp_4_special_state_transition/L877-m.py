#--coding:utf-8--

# dp[i][j]表示当剩下的石子堆为下标i到下标j时，当前玩家与另一个玩家的石子数量之差的最大值，注意当前玩家不一定是先手
# 只有当 i≤j 时，剩下的石子堆才有意义，因此当 i>j 时，dp[i][j] = 0。

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        length = len(piles)
        dp = [[0] * length for _ in range(length)]
        for i, pile in enumerate(piles):
            dp[i][i] = pile
        for i in range(length - 2, -1, -1):
            for j in range(i + 1, length):
                dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
        return dp[0][length - 1] > 0

# 智力题
# 先手每次选石头多的堆拿  先手稳赢
# return True