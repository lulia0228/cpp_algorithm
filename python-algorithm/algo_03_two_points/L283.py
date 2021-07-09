#--coding:utf-8--

class Solution:
    # def moveZeroes(self, nums: List[int]) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     i, j = 0, 0
    #     for j in range(len(nums)):
    #         if nums[j] != 0:
    #             nums[i] = nums[j]
    #             i += 1
    #     for k in range(i, len(nums)):
    #         nums[k] = 0

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        for j in range(len(nums)):
            if nums[j] != 0:
                # 直接交换更符合题意
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

