#--coding:utf-8--


class Solution:
    def findTargetSumWays(self, nums, S: int) -> int:
        sz = len(nums)
        tmp = sum(nums) + S
        if tmp % 2 or sum(nums) < S:
            return 0
        target = tmp // 2
        # dp[i][j]表示表示能用前i个物品[0,i-1]装满j容量的方法总数
        dp = [[0] * (target + 1) for i in range(sz + 1)]
        dp[0][0] = 1
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


