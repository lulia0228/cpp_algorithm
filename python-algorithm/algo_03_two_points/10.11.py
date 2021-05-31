#--coding:utf-8--

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)<=1: return
        nums.sort()
        if len(nums)%2 == 0:
            for i in range(0, len(nums), 2):
                nums[i], nums[i+1] = nums[i+1], nums[i]
        else:
            for i in range(0, len(nums)-1, 2):
                nums[i], nums[i+1] = nums[i+1], nums[i]

# 可以双指针