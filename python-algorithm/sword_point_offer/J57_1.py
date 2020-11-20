#--coding:utf-8--



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lt, rt = 0, len(nums)-1
        while lt < rt:
            tmp = nums[lt] + nums[rt]
            if tmp > target:
                rt -= 1
            elif tmp < target:
                lt += 1
            else:
                return [nums[lt], nums[rt]]
        return [-1, -1]