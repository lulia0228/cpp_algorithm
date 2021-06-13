# -*- coding: utf-8 -*-
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param nums int整型一维数组
# @param target int整型
# @return int整型
#

class Solution:
    def search(self , nums , target ):
        # write code here
        lt, rt = 0, len(nums)-1
        while lt <= rt:
            mid = lt +(rt-lt)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                rt = mid - 1
            else:
                lt = mid + 1
        return -1