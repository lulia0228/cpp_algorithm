#--coding:utf-8--
from typing import *

# 转化成 0-1背包
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        sz = len(nums)
        tmp = sum(nums) + S
        # 这道题前提条件说了元素是非负数
        if tmp % 2 or sum(nums)<S:
            return 0
        # 问题转化成在数组中找几个数字让它们的和为target由多少种组合,每个元素只用一次（01背包）
        target = tmp // 2 # target是大于0的
        # dp[i][j]表示表示能用前i个物品[0,i)装满j容量的方法种数
        dp = [[0] * (target + 1) for i in range(sz + 1)]
        dp[0][0] = 1
        # 外层遍历候选值；内层遍历约束
        for i in range(1, sz + 1):
            for j in range(target + 1):
                # 当前物品超过当前容量
                if nums[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    # 装入或者不装入当前物品
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
        return dp[sz][target]


# arr = [1,2,7,9,981]
arr = [0,0,0,0,0,0,0,0,1]
# s = 1000000000
s = 1
res = Solution().findTargetSumWays(arr, s)
print(res)


# 特殊设计，速度更快
class Solution:
    def findTargetSumWays(self, nums, S: int) -> int:
        sz = len(nums)
        tmp = sum(nums) + S
        if tmp % 2 or sum(nums) < S:
            return 0
        target = tmp // 2
        dp = [0] * (target + 1)
        dp[0] = 1
        # 假如给定nums = [num1,num2,num3]，则有dp[j] = dp[j-num1] + dp[j-num2] + dp[j-num3].
        # 经过转化后，题目就变成了在数组num中选择一个子集使它们的和为target。看着有点像硬币找零组合数，不过不是，区别在于
        # 这里每个元素只能使用1次，硬币找零的时候，每种硬币使用次数无限制
        for i in range(sz): # 每个元素只用1次
            # 倒序遍历
            for j in range(target, nums[i]-1, -1):
                dp[j] += dp[j - nums[i]]
        return dp[target]

class Solution1:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        sz = len(nums)
        tmp = sum(nums) + S
        # 这道题前提条件说了元素是非负数
        if tmp % 2 or sum(nums)<S:
            return 0
        # 问题转化成在数组中找几个数字让它们的和为target由多少种组合,每个元素只用一次（01背包）
        target = tmp // 2 # target是大于0的
        # 这里尝试回溯会超时；回溯问题参考组合总和39 40 区别是它们数组里都是正整数，没有0
        res = []
        nums.sort(reverse=True)
        cnt_zero = 0
        for i in range(len(nums)-1, -1, -1):
            if nums[i] != 0: break
            cnt_zero += 1
        self.dfs(target, nums, 0, 0, [], res)
        # n个0的子集数除了空集为pow(2,n)-1
        return len(res)*(1+pow(2,cnt_zero)-1)

    def dfs(self, target, nums, idx, cur_sum, tmp, res):
        if cur_sum == target:
            res.append(tmp[:])
            return
        for i in range(idx, len(nums)):
            tmp.append(nums[i])
            self.dfs(target, nums, i+1, cur_sum+nums[i], tmp, res)
            tmp.pop()

arr = [25,18,47,13,45,29,15,45,33,19,39,15,39,45,17,21,29,43,50,10]
arr += [0, 0, 0 , 0] # 86272
s = 25
res = Solution1().findTargetSumWays(arr, s)
print(res)

arr = [0, 0, 0, 0] # 86272
s = 0
res = Solution1().findTargetSumWays(arr, s)
print(res)