#--coding:utf-8--

# 2 2 2 0 1 这种情况无需特殊考虑 153的解法就可以处理

# 需要处理的是旋转数组是从重复数字中的某一位置断开的特殊情况 如 2 0 1 2 2  或者 2 2 0 1 2
# 处理的方法就是把后面数组的重复末尾给删除掉(不需要真的删除掉，索引处理即可)，形成一个新的数组，
# 然后按照153的方法处理新的数组

class Solution:
    def findMin(self, nums: List[int]) -> int:
        lt, rt = 0, len(nums) - 1
        if nums[0] < nums[rt]:
            return nums[0]
        elif nums[0] > nums[rt]:
            while lt < rt:
                mid = lt + (rt - lt) // 2
                if nums[mid] <= nums[rt]:
                    rt = mid
                else:
                    lt = mid + 1
        elif nums[0] == nums[rt]:
            while rt > 0 and nums[rt] == nums[len(nums) - 1]:
                rt -= 1
            while lt < rt:
                mid = lt + (rt - lt) // 2
                if nums[mid] <= nums[rt]:
                    rt = mid
                else:
                    lt = mid + 1

        return nums[lt]