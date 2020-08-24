#--coding:utf-8--
'''
@Time   : 2019/8/24
@Author : Heng Li
@Email  : liheng_lulia@163.com
'''

# 必须要排序，否则没法用下面的办法去重

class Solution:
    def __init__(self, **kwargs):
        self.res = []
        self.flag = []

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.flag = [False for i in range(len(nums))]
        nums.sort()
        self.dfs(nums, 0, [])
        return self.res

    def dfs(self, nums, idx, cur_ls):
        if idx == len(nums):
            self.res.append(cur_ls[:])
            return
        for i in range(len(nums)):
            if not self.flag[i]:
                # 去重，最重要的条件：not self.flag[i-1]
                if i>0 and nums[i]==nums[i-1] and not self.flag[i-1]:
                    continue
                cur_ls.append(nums[i])
                self.flag[i] = True
                self.dfs(nums, idx+1, cur_ls)
                cur_ls.pop()
                self.flag[i] = False