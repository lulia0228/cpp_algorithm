# -*- coding: utf-8 -*-


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            tmp = target-nums[i]
            if tmp in d:
                return [d[tmp], i]
            # 放在判断后插入字典是为了防止自身被重复使用
            d.update({nums[i]: i})
        return [-1,-1]
