# -*- coding: utf-8 -*-
#
# max length of the subarray sum = k
# @param arr int整型一维数组 the array
# @param k int整型 target
# @return int整型
#

class Solution:
    def maxlenEqualK(self, arr, k):
        # write code here
        r_d = {0: -1}  # 容易漏掉数组起始点为0的情况。必须加上0：-1
        ans = 0
        sum_ = 0
        for i in range(len(arr)):
            sum_ += arr[i]
            if sum_ - k in r_d:
                ans = max(ans, i - r_d[sum_ - k])
            if sum_ not in r_d:  # 只记录sum_一个出现的索引
                r_d[sum_] = i
        return ans

# 扩展问题1：
# 给定一个无序数组arr 其中元素可正、可负、可0。求arr所有的子数组中正数与负数个数相等的最长数组长度。
# 解：将arr中的正数变为1，负数变为-1，0不变，然后求累加和为0的最长子数组。

# 扩展问题2：
# 给定一个无序数组arr 其中元素只能是1或者0。求arr所有的子数组中0和1个数相等的最长数组长度。
# 解：将arr中的0变为-1，1不变，然后求累加和为0的最长子数组。