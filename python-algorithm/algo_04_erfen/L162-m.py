#--coding:utf-8--


# 题目要求只需要返回一个峰值的下标

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lt = 0
        rt = len(nums)-1;
        while lt < rt :
            mid = lt+(rt-lt)//2;
            if nums[mid] > nums[mid+1]: # 中点是降序，说明峰值在左边，因此更新右边界
                rt = mid
            else:
                lt = mid+1
        return lt # 最终lt rt一样


# 题目要求只需要返回一个峰值；下面的也可以，只是时间复杂度不是logn；找到的是第一个破坏升序的
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return i
        return len(nums)-1