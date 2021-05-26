#--coding:utf-8--

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        sz = len(nums)
        j = 1
        for i in range(0, sz, 2):
            if nums[i] % 2 == 1:
                while nums[j]%2 == 1:
                    j += 2
                nums[i], nums[j] = nums[j], nums[i]
        return nums
