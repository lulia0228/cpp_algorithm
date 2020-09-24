#--coding:utf-8--
'''
@Time   : 2020/9/24
@Author : Heng Li
@Email  : liheng_lulia@163.com
'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[cnt] = nums[j]
                cnt += 1
        while cnt < len(nums):
            nums[cnt] = 0
            cnt += 1