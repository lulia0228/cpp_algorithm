# -*- coding: utf-8 -*-
# @Time    : 2020/10/4 19:21
# @Author  : No Name

# 搞了2个数组分别记录当前元素左右两侧的数字乘积，空间复杂度是O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        c = [1 for i in range(len(nums))]
        d = [1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            c[i] = c[i-1]*nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            d[i] = d[i+1]*nums[i+1]
        for i in range(len(nums)):
            res.append(c[i]*d[i])
        return res

# 题目说了用于存放输出结果的数组不算空间复杂度
# 那就先用输出数组存放c 然后反向遍历过程中动态构造右侧乘积，直接相乘存放最终的输出结果

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            res[i] = res[i-1]*nums[i-1]
        tmp = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i]*tmp
            tmp = tmp*nums[i]
        return res