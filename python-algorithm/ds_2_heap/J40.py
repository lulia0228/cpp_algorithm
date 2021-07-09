#--coding:utf-8--

# 找到数组中最小的k个数字

class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        lt, rt = 0, len(arr)-1
        while lt <= rt:
            mid = self.partition(arr, lt, rt)
            if mid == k:
                return arr[:k]
            elif mid > k-1:
                rt = mid-1
            else:
                lt = mid+1
        # k==len(arr)的时候，需要单独返回全部，前面无法找到mid==k
        return arr

    def partition(self, arr, lt, rt):
        pivot = arr[lt]
        while lt<rt:
            while lt<rt and arr[rt]>=pivot:
                rt -= 1
            arr[lt] = arr[rt]
            while lt<rt and arr[lt]<=pivot:
                lt += 1
            arr[rt] = arr[lt]
        arr[lt] = pivot
        return lt