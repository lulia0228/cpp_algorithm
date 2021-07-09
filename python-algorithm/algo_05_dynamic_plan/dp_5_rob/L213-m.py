#--coding:utf-8--

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        # 不偷第一个房子和不偷最后一个房子
        amount1 = self.exec(nums[:-1])
        amount2 = self.exec(nums[1:])
        return max(amount1, amount2)

    def exec(self, nums):
        print(nums)
        sz = len(nums)
        dp = [0] * (sz + 1)
        dp[1] = nums[0]
        for i in range(2, sz + 1):
            # if else 应该括起来，否则运算优先级会改变掉逻辑
            dp[i] = max(dp[i - 1], (dp[i - 2] if i >= 2 else 0) + nums[i - 1])
        return dp[sz]