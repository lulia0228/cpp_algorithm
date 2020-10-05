# -*- coding: utf-8 -*-
# @Time    : 2020/10/5 11:09
# @Author  : No Name

# 使用3个哈希，1个标记元素出现频次，1个标记元素第1次出现位置，1个标记元素最后一次出现位置
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d1, d2, d3 ={}, {}, {}
        for i in range(len(nums)):
            if nums[i] not in d1:
                d1[nums[i]] = 1
            else:
                d1[nums[i]] += 1
            if nums[i] not in d2:
                d2[nums[i]] = i
            d3[nums[i]] = i
        min_len = len(nums)
        degree = 1
        for k,v in d1.items():
            if v>degree:
                degree = v
                min_len = d3[k]-d2[k]+1
                # 最高频词有多个的时候
            elif v==degree:
                min_len = min(min_len, d3[k]-d2[k]+1)
        return min_len