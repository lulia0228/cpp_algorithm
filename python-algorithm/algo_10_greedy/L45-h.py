# -*- coding: utf-8 -*-


class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        end = 0
        fartest = nums[0]
        for i in range(len(nums)-1):
            fartest = max(fartest, nums[i]+i)
            if end == i:
                jumps += 1
                end = fartest
        return jumps


# 牛客148
class Solution:
    def Jump(self, n, A):
        # write code here
        cnt = 0
        far, end = 0, 0
        for i, num in enumerate(A):
            far = max(far, i + num)
            if end >= n:
                break
            if end == i:
                end = far
                cnt += 1
        return cnt

