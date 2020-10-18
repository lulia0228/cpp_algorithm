#--coding:utf-8--


# dp[i]表示以A[i]作为结尾的等差子序列的个数
# 注意理解上面这句话：  1 2 3 4 5
# dp[4] = dp[3] + 1
# dp[3]: 1 2 3 4 // 2 3 4
# dp[4]: 1 2 3 4 5 // 2 3 4 5 // 3 4 5(多出来的就是最后一个)
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        sz = len(A)
        if sz < 3:
            return 0
        # dp[i]表示以A[i]作为结尾的等差子序列的个数
        dp = [0]*sz
        for i in range(2, sz):
            if A[i]-A[i-1] == A[i-1]-A[i-2]:
                dp[i] = dp[i-1]+1
        return sum(dp)