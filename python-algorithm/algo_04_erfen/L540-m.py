#--coding:utf-8--
'''
@Time   : 2020/9/25
@Author : Heng Li
@Email  : liheng_lulia@163.com
'''

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lt, rt = 0, len(nums)-1
        while lt < rt:
            mid = lt + (rt-lt)//2
            if mid%2 == 0:
                if nums[mid] == nums[mid-1]:
                    rt = mid-2
                else:
                    lt = mid
            else:
                if nums[mid] == nums[mid-1]:
                    lt = mid + 1
                else:
                    rt = mid - 1
        return nums[lt]