#--coding:utf-8--


class Solution:
    def findMin(self, nums: List[int]) -> int:
        lt, rt = 0, len(nums)-1
        if nums[0] < nums[rt]:
            return nums[0]
        while lt < rt:
            mid = lt + (rt-lt)//2
            if nums[mid] <= nums[rt]:
                rt = mid
            else:
                lt = mid + 1
        return nums[lt]


