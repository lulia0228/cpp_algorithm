# -*- coding: utf-8 -*-
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sz = len(nums)
        if sz < 3: return []
        nums.sort()
        if nums[0] > 0 or nums[-1] < 0: return []
        res = []
        for i in range(sz - 2):
            # 去掉以相同值开始的重复情况
            if i > 0 and nums[i] == nums[i - 1]: continue
            lt, rt = i + 1, sz - 1
            while lt < rt:
                s = nums[lt] + nums[rt] + nums[i]
                if s > 0:
                    rt -= 1
                elif s < 0:
                    lt += 1
                else:
                    res.append([nums[i], nums[lt], nums[rt]])
                    # 去除双指针区间内的重复情况  (不能去掉)
                    while lt < rt and nums[lt + 1] == nums[lt]:
                        lt += 1
                    # attention: lt<rt 条件应该放在and之前 防止索引取值越界错误
                    while lt < rt and nums[rt - 1] == nums[rt]:
                        rt -= 1
                    lt += 1
                    rt -= 1
        return res
