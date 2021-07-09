#--coding:utf-8--


#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        peak = 0
        sz = mountain_arr.length()
        lt, rt = 0, sz - 1
        while lt < rt:
            mid = lt + (rt - lt) // 2
            if mountain_arr.get(mid) > mountain_arr.get(mid + 1):
                rt = mid
            else:
                lt = mid + 1
        peak = rt

        left_idx = self.binary_search(mountain_arr, 0, peak, target, lambda x: x)
        right_idx = self.binary_search(mountain_arr, peak, sz - 1, target, lambda x: -x)
        if left_idx == -1 and right_idx == -1:
            return -1
        if left_idx == -1:
            return right_idx
        if right_idx == -1:
            return left_idx
        return min(left_idx, right_idx)

    def binary_search(self, mountain_arr, lt, rt, target, func):
        targ = func(target)
        while lt <= rt:
            mid = lt + (rt - lt) // 2
            tmp = func(mountain_arr.get(mid))
            if tmp == targ:
                return mid
            elif tmp > targ:
                rt = mid - 1
            else:
                lt = mid + 1
        return -1
