#--coding:utf-8--


#第一套方法逻辑；while lt<rt
'''
满足条件的都写l = mid 或者 r = mid，
mid首先写成l + r >> 1，如果满足条件选择的是l = mid，那么mid那里就加个1，写成l + r + 1 >> 1。
然后就是else对应的写法l = mid 对应r = mid - 1; r = mid 对应 l = mid + 1.
'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums == [] or nums[0] > target or nums[-1] < target:
            return [-1, -1]
        start = self.find_start(nums, target)
        # 说明数组中没有target,也没必要再去找最后一次出现的target
        if start == -1:
            return [-1, -1]
        end = self.find_end(nums, target)
        return [start, end]

    # 查找第一个大于等于target的索引
    def find_start(self, nums, target):
        lt, rt = 0, len(nums) - 1
        while lt < rt:
            # mid = lt + (rt-lt)//2
            mid = (lt + rt) >> 1
            if nums[mid] >= target:
                rt = mid
            else:
                lt = mid + 1
        if nums[rt] != target:
            return -1
        return rt

    # 查找最后一个小于等于target的索引
    def find_end(self, nums, target):
        lt, rt = 0, len(nums) - 1
        while lt < rt:
            # mid = lt + (rt-lt+1)//2
            mid = (lt + rt + 1) >> 1
            if nums[mid] <= target:
                lt = mid
            else:
                rt = mid - 1
        if nums[lt] != target:
            return -1
        return lt


#第二套方法逻辑；while lt<=rt
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums == []:
            return [-1, -1]
        start = self.find_start(nums, target)
        end = self.find_end(nums, target)
        return [start, end]

    # 查找第一个大于等于target的索引
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

    # 查找最后一个小于等于target的索引
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