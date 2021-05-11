#--coding:utf-8--

from typing import  *
# 二分找到第一个大于x的值，然后在x前后[x-k, x+k-1]范围内双指针排除较大的值，剩下的即为所求
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        if x <= arr[0]:
            return arr[:k]
        elif x >= arr[-1]:
            return arr[-k:]
        else:
            first_bigger = self.find_first_bigger(arr, x)
            print(first_bigger)

            lt_border = first_bigger-k if first_bigger>=k else 0
            rt_border = first_bigger+k-1 if first_bigger+k-1<len(arr) else len(arr)-1

            while rt_border-lt_border + 1 > k:
                if x-arr[lt_border]<= arr[rt_border]-x:
                    rt_border -= 1
                else:
                    lt_border += 1

        return arr[lt_border:rt_border+1]


    def find_first_bigger(self, nums, target):
        lt, rt = 0, len(nums) - 1
        while lt <= rt:
            mid = lt + (rt - lt) // 2
            if nums[mid] <= target: # 第一个＞
            # if nums[mid] < target:    # 第一个≥
                lt = mid + 1
            else:
                rt = mid - 1
        if lt < len(nums):
            return lt
        return -1


class Solution1:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = []
        if x <= arr[0]:
            return arr[:k]
        elif x >= arr[-1]:
            return arr[-k:]
        else:
            first_bigger = self.find_first_bigger(arr, x)
            first_smaller = self.find_first_smaller(arr, x)
            # print(first_bigger, first_smaller)

            cnt = 0
            if first_bigger == first_smaller:
                cnt += 1
                res = res + [arr[first_smaller]]
                first_smaller -= 1
                first_bigger += 1

            elif first_bigger < first_smaller:
                cnt += first_smaller-first_bigger+1
                res = res + arr[first_bigger:first_smaller+1]
                tmp = first_bigger
                first_bigger = first_smaller + 1
                first_smaller = tmp - 1

            while cnt < k and first_smaller >= 0 and first_bigger<len(arr):
                if x-arr[first_smaller] <= arr[first_bigger]-x:
                    res = [arr[first_smaller]] + res
                    first_smaller -= 1
                else:
                    res = res + [arr[first_bigger]]
                    first_bigger += 1
                cnt += 1

            if cnt < k:
                if first_smaller == -1:
                    res = res + arr[first_bigger:first_bigger+k-cnt]
                elif first_bigger == len(arr):
                    res = arr[first_smaller+1-k+cnt:first_smaller+1] + res

        return res


    def find_first_bigger(self, nums, target):
        lt, rt = 0, len(nums) - 1
        while lt <= rt:

            mid = lt + (rt - lt) // 2
            # if nums[mid] <= target: # 第一个＞
            if nums[mid] < target:    # 第一个≥
                lt = mid + 1
            else:
                rt = mid - 1
        if lt < len(nums):
            return lt
        return -1


    def find_first_smaller(self, nums, target):
        lt, rt = 0, len(nums) - 1
        while lt <= rt:

            mid = lt + (rt - lt) // 2
            # if nums[mid] >= target: # 第一个＜
            if nums[mid] > target:    # 第一个≤
                rt = mid - 1
            else:
                lt = mid + 1
        if rt >= 0:
            return rt
        return -1


if __name__ == "__main__":
    arr = [1,2,5,5,6,6,7,7,8,9]
    # arr = [0,1,1,1,2,3,6,7,8,9]
    # arr = [1,2,3,4]
    k, x = 7, 7
    # k, x = 9, 4
    # k, x = 4, 3
    res = Solution().findClosestElements(arr, k, x)
    print(res)