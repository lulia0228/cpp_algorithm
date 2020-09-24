#--coding:utf-8--
'''
@Time   : 2020/9/24
@Author : Heng Li
@Email  : liheng_lulia@163.com
'''


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        sz = len(nums)
        res = []
        if sz < 3 or nums[0] > 0 or nums[sz - 1] < 0:
            return []
        for i in range(sz):
            # 去掉以相同值开始的重复情况
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            lt, rt = i + 1, sz - 1
            while lt < rt:
                s = nums[i] + nums[lt] + nums[rt]
                if s > 0:
                    rt -= 1
                elif s < 0:
                    lt += 1
                else:
                    res.append([nums[i], nums[lt], nums[rt]])
                    # 去除双指针区间内的重复情况
                    while lt < rt and nums[lt + 1] == nums[lt]:
                        lt += 1
                    # attention: lt<rt 条件应该放在and之前 防止索引取值越界错误
                    while lt < rt and nums[rt - 1] == nums[rt]:
                        rt -= 1
                    lt += 1
                    rt -= 1
        return res

