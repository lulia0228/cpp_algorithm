#--coding:utf-8--
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lt, rt = 0, len(nums)-1
        while lt<rt:
            nums[lt], nums[rt] = nums[rt], nums[lt]
            lt += 1
            rt -= 1
        flag = k%len(nums)
        lt, rt = 0, flag-1
        while lt<rt:
            nums[lt], nums[rt] = nums[rt], nums[lt]
            lt += 1
            rt -= 1
        lt, rt = flag, len(nums)-1
        while lt<rt:
            nums[lt], nums[rt] = nums[rt], nums[lt]
            lt += 1
            rt -= 1