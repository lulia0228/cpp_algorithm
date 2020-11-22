# -*- coding: utf-8 -*-


# 数组中的逆序对
# 和leetcode315求数组中每个元素右侧小于它的元素个数一样

class Solution:
    def __init__(self, *args, **kwargs):
        self.res = 0

    def reversePairs(self, nums: List[int]) -> int:
        info = []
        lenth = len(nums)
        self.gb_sort(nums, 0, lenth - 1)
        return self.res

    def gb_sort(self, nums, left, right):
        if left >= right:
            return;
        mid = left + (right - left) // 2;
        self.gb_sort(nums, left, mid)
        self.gb_sort(nums, mid + 1, right)
        self.merge(nums, left, mid, right)

    def merge(self, nums, left, mid, right):
        i, j = left, mid + 1
        tmp_nums = []
        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                tmp_nums.append(nums[i])
                # 即后半部分数组从mid+1到j-1都是小于nums[i][0]的
                self.res += j - mid - 1
                i += 1
            else:
                tmp_nums.append(nums[j])
                j += 1

        if j == right + 1:
            for k in range(i, mid + 1):
                self.res += j - mid - 1
                tmp_nums.append(nums[k])
        else:
            for h in range(j, right + 1):
                tmp_nums.append(nums[h])

        m, n = 0, left
        while m < len(tmp_nums):
            nums[n] = tmp_nums[m]  # 每次小合并后在原数组上相应位置赋值
            n += 1
            m += 1