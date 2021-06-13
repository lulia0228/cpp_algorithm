# -*- coding: utf-8 -*-
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 找缺失数字
# @param a int整型一维数组 给定的数字串
# @return int整型
#

# 方法1 二分法
class Solution:
    def solve(self , a ):
        # write code here
        lt, rt = 0, len(a)-1
        if a[-1]<len(a):
            return len(a)
        while lt < rt:
            mid = lt +(rt-lt)//2
            if a[mid] == mid:
                lt = mid+1
            else:
                rt = mid
        return lt

class Solution1:
    def solve(self, a):
        # write code here
        lt, rt = 0, len(a) - 1
        while lt <= rt:
            mid = lt + (rt - lt) // 2
            if a[mid] == mid:
                lt = mid + 1
            else:
                rt = mid - 1
        return lt

# 方法2 位运算
class Solution:
    def solve(self , a ):
        # write code here
        res = 0
        for i in range(len(a)):
            res = res^i^a[i]
        return res^len(a)