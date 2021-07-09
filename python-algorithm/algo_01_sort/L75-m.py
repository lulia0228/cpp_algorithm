#--coding:utf-8--

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        i, j = 0, n - 1
        k = 0
        while k <= j:
            while k <= j and nums[k] == 2:
                nums[k], nums[j] = nums[j], nums[k]
                j -= 1
            # 2和后面换完后 可能变成0 要处理0
            if nums[k] == 0:
                nums[k], nums[i] = nums[i], nums[k]
                i += 1
            k += 1

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, len(nums)-1
        k = 0
        while k <= j:
            if nums[k] == 0:
                nums[k], nums[i] = nums[i], nums[k]
                i += 1
                k += 1
            elif nums[k] == 2:
                nums[k], nums[j] = nums[j], nums[k]
                j -= 1
            else:
                k += 1

# 哈希法
class Solution1:
    def sortColors(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = [0,0,0]
        lenth = len(nums)
        for i in range(lenth):
            if nums[i] == 0:
                cnt[0] += 1
            elif nums[i] == 1:
                cnt[1] += 1
            else:
                cnt[2] += 1
        for i in range(lenth):
            if i<cnt[0]:
                nums[i] = 0
            elif i>=cnt[0] and i<cnt[1]+cnt[0]:
                nums[i] = 1
            else:
                nums[i] = 2

a = [2,0,2,1,1,0]
Solution().sortColors(a)
print(a)