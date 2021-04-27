#--coding:utf-8--
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        lt, rt = 0, mountain_arr.length()-1
        while lt<rt:
            mid = lt +(rt-lt)//2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                lt = mid+1
            else:
                rt = mid
        peak = lt
        index = self.binary_serach(mountain_arr, target, 0, peak, func=lambda x:x)
        if index == -1:
            index = self.binary_serach(mountain_arr, target, peak+1, mountain_arr.length()-1, func=lambda x:-x)
        return index

    def binary_serach(self, mountain_arr, target, lt, rt, func = lambda x:x):
        target = func(target)
        while lt<=rt:
            mid = lt + (rt - lt) // 2
            if func(mountain_arr.get(mid))<target:
                lt = mid+1
            elif func(mountain_arr.get(mid))>target:
                rt = mid-1
            else:
                return mid
        return -1