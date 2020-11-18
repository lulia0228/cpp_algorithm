#--coding:utf-8--

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            res = res^i^nums[i]
        return res^len(nums)