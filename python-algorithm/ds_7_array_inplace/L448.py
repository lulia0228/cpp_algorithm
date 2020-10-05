# -*- coding: utf-8 -*-
# @Time    : 2020/10/5 8:22
# @Author  : No Name


# 题目要求不使用额外空间；所以就不能用哈希标记

class Solution:
    def findDisappearedNumbers(self, nums) :
        res = []
        for i in range(len(nums)):
            if nums[i] != i+1:
                while nums[i] != nums[nums[i]-1]:
                    # 下面这句话达不到想要交换2个下标值的目的，因为第2个下标用到了nums[i],
                    # 而nums[i]在第一个下标处已经被改变；因此第二个下标不是实际要交换的下标了
                    # nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i]
                    # 用一个变量记录下nums[i]确保第二个下标不会因为第一个下标值的变化而变化
                    tmp = nums[i]
                    nums[i], nums[tmp-1] = nums[tmp-1], nums[i]
        for i in range(len(nums)):
            if nums[i] != i+1:
                res.append(i+1)
        return res


# 把 |nums[i]|-1 索引位置的元素标记为负数。即nums[∣nums[i]∣−1]×−1 。
# 然后遍历数组，若当前数组元素 nums[i] 为负数，说明我们在数组中存在数字 i+1。

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            new_index = abs(nums[i]) - 1
            if nums[new_index] > 0:
                nums[new_index] *= -1
        result = []
        for i in range(1, len(nums) + 1):
            if nums[i - 1] > 0:
                result.append(i)
        return result

nums =[4,3,2,7,8,2,3,1]
res = Solution().findDisappearedNumbers(nums)
print(res)