#--coding:utf-8--
'''
@Time   : 2019/8/24
@Author : Heng Li
@Email  : liheng_lulia@163.com
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, idx, cur_ls, res):
        # res.append(cur_ls[:])
        for i in range(idx, len(nums)):
            cur_ls.append(nums[i])
            self.dfs(nums, i + 1, cur_ls, res)
            cur_ls.pop()
        res.append(cur_ls[:])