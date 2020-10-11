#--coding:utf-8--
'''
@Time   : 2020/10/10
@Author : No Name
'''

# 题目转化成了和494：从非负整数数组中选取一部分数字使他们和为Target,共有多少种选择方法？
# 和494存在细微区别在于 这里数组中是正整数，不是非负整数，另外只是判断是否存在这样的一个选择？

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


# 特殊设计的
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sz = len(nums)
        if sum(nums) % 2:
            return False
        target = sum(nums) // 2
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(sz): # 每个元素只能用1次
            # 倒序遍历
            for j in range(target, nums[i]-1, -1):
                    if dp[j-nums[i]] == 1:
                        dp[j] = 1
        return dp[target]==1



