#--coding:utf-8--

class Solution:
    def rob(self, nums: List[int]) -> int:
        sz = len(nums)
        dp = [0]*(sz+1)
        for i in range(1, sz+1):
            dp[i] = max(dp[i-1], (dp[i-2] if i-2>=0 else 0)+nums[i-1])
        return dp[sz]