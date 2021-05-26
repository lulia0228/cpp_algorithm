#--coding:utf-8--


# 算贪心算法

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        sz = len(nums)
        if sz < 3:
            return False
        small = mid = inf
        for i in range(sz):
            if nums[i] <= small:
                small = nums[i]
            elif nums[i] <= mid:
                mid = nums[i]
            else:
                return True
        return False