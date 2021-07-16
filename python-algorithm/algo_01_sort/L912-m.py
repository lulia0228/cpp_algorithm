#--coding:utf-8--
# 快排 归并 堆排序
#--coding:utf-8--
from typing import *
# (1) 快排
import random
class Solution:
    def MySort(self, nums):
        # write code here
        return self.QuickSort(nums, 0, len(nums) - 1)

    def QuickSort(self, nums, lt, rt):
        if lt >= rt: return
        # partiton功能2个：部分排序数组；返回分界点下标
        # 可以在这里直接写函数体，不用单独调函数也可以
        mid = self.partition(nums, lt, rt)
        self.QuickSort(nums, lt, mid - 1)
        self.QuickSort(nums, mid + 1, rt)
        return nums

    def partition(self, nums, lt, rt):
        # 直接选取左端点作为枢轴
        # pivot = nums[lt]
        # 随机先选一个值，然后交换到两个端点的一个
        pivot_idx = random.randint(lt, rt)
        nums[lt], nums[pivot_idx] = nums[pivot_idx], nums[lt]
        pivot = nums[lt]
        while lt < rt:
            # 从右往左找到第一个小于pivot的值
            while rt > lt and nums[rt] >= pivot:
                rt -= 1
            nums[lt] = nums[rt]
            # 从左往右找到第一个大于pivot的值
            while lt < rt and nums[lt] <= pivot:
                lt += 1
            nums[rt] = nums[lt]
        nums[lt] = pivot
        return lt


#（2）归并排序
# 合并时候创建了新数组；不创建新数组的写法可用以求逆序对？？
class Solution1:
    def MySort(self, nums):
        # write code here
        return self.GbSort(nums, 0, len(nums) - 1)

    def GbSort(self, nums, lt, rt):
        if lt >= rt: return [nums[lt]]
        mid = lt + (rt - lt) // 2
        s1 = self.GbSort(nums, lt, mid)
        s2 = self.GbSort(nums, mid + 1, rt)
        return self.merge(s1, s2)

    def merge(self, s1, s2):
        new_nums = []
        i, j = 0, 0
        while i < len(s1) and j < len(s2):
            if s1[i] <= s2[j]:
                new_nums.append(s1[i])
                i += 1
            else:
                new_nums.append(s2[j])
                j += 1
        if i < len(s1):
            for k in range(i, len(s1)):
                new_nums.append(s1[k])
        else:
            for k in range(j, len(s2)):
                new_nums.append(s2[k])
        return new_nums


class Solution2:
    def MySort(self, nums):
        # write code here
        self.GbSort(nums, 0, len(nums) - 1)
        return nums

    def GbSort(self, nums, lt, rt):
        if lt >= rt: return
        mid = lt + (rt - lt) // 2
        self.GbSort(nums, lt, mid)
        self.GbSort(nums, mid + 1, rt)
        self.merge(nums, lt, mid, rt)

    def merge(self, nums, left, mid, right):
        tempArray = [0] * (right - left + 1)  # 临时数组
        i, j, k = left, mid + 1, 0
        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                tempArray[k] = nums[i]
                i += 1
            else:
                tempArray[k] = nums[j]
                j += 1
            k += 1
        while i <= mid:
            tempArray[k] = nums[i]
            k += 1
            i += 1
        while j <= right:
            tempArray[k] = nums[j]
            k += 1
            j += 1
        for x in range(k):  # 将排序好的数组放回原来的数组
            nums[left + x] = tempArray[x]


#（3）堆排序
class Solution3:
    def max_heapify(self, heap, root, heap_len):
        p = root
        while p * 2 + 1 < heap_len:
            l, r = p * 2 + 1, p * 2 + 2
            if heap_len <= r or heap[r] < heap[l]:
                nex = l
            else:
                nex = r
            if heap[p] < heap[nex]:
                heap[p], heap[nex] = heap[nex], heap[p]
                p = nex
            else:
                break

    def build_heap(self, heap):
        for i in range(len(heap) - 1, -1, -1):
            self.max_heapify(heap, i, len(heap))

    def heap_sort(self, nums):
        self.build_heap(nums)
        for i in range(len(nums) - 1, -1, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.max_heapify(nums, 0, i)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.heap_sort(nums)
        return nums


arr = [4,5,6,8,9]
res = Solution3().sortArray(arr)
print(res)