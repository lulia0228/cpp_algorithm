#--coding:utf-8--
'''
@Time   : 2020/10/10
@Author : No Name
'''

# 注意：0-1背包问题每个元素是不可以复用的，即每个元素只可以用1次

# 416. 分割等和子集
# 题目：从正整数数组中选取一部分元素，使得他们的和为数组总和的一半。

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sz = len(nums)
        if sum(nums) % 2:
            return False
        target = sum(nums) // 2
        # dp[i][j]表示表示能否用前i个物品[0,i-1]装满j容量
        dp = [[0] * (target + 1) for i in range(sz + 1)]
        for i in range(sz + 1):
            dp[i][0] = 1
        for i in range(1, sz + 1):
            for j in range(1, target + 1):
                # 当前物品超过当前容量
                if nums[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    # 装入或者不装入当前物品
                    dp[i][j] = (dp[i - 1][j] or dp[i - 1][j - nums[i - 1]])
        return dp[sz][target]==1





