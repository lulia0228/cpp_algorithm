# -*- coding: utf-8 -*-


# 1 暴力法 不借助额外空间 旋转k次 超时
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sz = len(nums)
        k = k%sz
        for i in range(k):
            record = nums[-1]
            for j in range(sz-1, 0, -1):
                nums[j] = nums[j-1]
            nums[0] = record

# 2 用额外空间存放每个元素应该在的位置，最后复制到原始数组
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sz = len(nums)
        tmp_ls = [0 for i in range(sz)]
        for i in range(sz):
            tmp_ls[(i+k)%sz] = nums[i]
        for i in range(sz):
            nums[i] = tmp_ls[i]

# 3 翻转3次
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sz = len(nums)
        k = k%sz
        for i in range(sz//2):
            nums[i], nums[sz-i-1] = nums[sz-i-1], nums[i]
        for i in range(k//2):
            nums[i], nums[k-i-1] = nums[k-i-1], nums[i]
        for i in range(k, k+(sz-k)//2):
            nums[i], nums[k+(sz-i-1)] = nums[k+(sz-i-1)], nums[i]
