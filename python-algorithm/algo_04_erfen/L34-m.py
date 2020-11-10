#--coding:utf-8--

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums == []:
            return [-1, -1]
        start = self.find_start(nums, target)
        end = self.find_end(nums, target)
        return [start, end]

    def find_start(self, nums, target):
        lt, rt = 0, len(nums)-1
        while lt <= rt:
            mid = lt + (rt-lt)//2
            if nums[mid] < target:
                lt = mid + 1
            else:
                rt = mid - 1
        if lt < len(nums) and nums[lt] == target:
            return lt
        return -1

    def find_end(self, nums, target):
        lt, rt = 0, len(nums)-1
        while lt <= rt:
            mid = lt + (rt-lt)//2
            if nums[mid] > target:
                rt = mid - 1
            else:
                lt = mid + 1
        if rt >= 0 and nums[rt] == target:
            return rt
        return -1