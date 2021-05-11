#--coding:utf-8--

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3: return n
        flag = nums[0]
        i, j = 1, 1
        cnt = 1
        for j in range(1, n):
            if nums[j] == flag:
                cnt += 1
            else:
                flag = nums[j]
                cnt = 1
            if cnt < 3:
                nums[i] = nums[j]
                i += 1
        return i