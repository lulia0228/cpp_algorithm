#--coding:utf-8--



class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max2 = max1 = 0
        for i in range(len(nums)):
            if nums[i] > max1:
                max2 = max1
                max1 = nums[i]
            elif nums[i]<=max1 and nums[i]>max2:
                max2 = nums[i]
        return (max2-1)*(max1-1)
