#--coding:utf-8--

# leetcode 704 二分查找

class Solution:
    # 1 是否存在target
    def search(self, nums: List[int], target: int) -> int:
        lt, rt = 0, len(nums)-1
        while lt <= rt:
            mid = lt + (rt -lt)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                rt = mid - 1
            else:
                lt = mid + 1
        return -1

    # 2 查找第1个出现的target
    def find_first(self, nums, target):
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

    # 3 查找最后1个出现的target
    def find_last(self, nums, target):
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

    # 4 查找第1个＞或者≥target的元素
    def find_first_bigger(self, nums, target):
        lt, rt = 0, len(nums) - 1
        while lt <= rt:
            mid = lt + (rt - lt) // 2
            # if letters[mid] <= target: # 第一个＞
            if letters[mid] < target:    # 第一个≥
                lt = mid + 1
            else:
                rt = mid - 1
        if lt < len(letters):
            return letters[lt]
        return -1

    # 4 查找第1个＜或者≤target的元素
    def find_first_smaller(self, nums, target):
        lt, rt = 0, len(nums) - 1
        while lt <= rt:
            mid = lt + (rt - lt) // 2
            # if letters[mid] >= target: # 第一个＜
            if nums[mid] > target:    # 第一个≤
                rt = mid - 1
            else:
                rt = mid + 1
        if rt >= 0:
            return letters[rt]
        return -1