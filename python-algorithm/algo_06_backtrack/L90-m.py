#--coding:utf-8--
'''
@Time   : 2019/8/24
@Author : Heng Li
@Email  : liheng_lulia@163.com
'''

# 方法1 子集78的做法 然后用set去重
# 方法2 先排序，然后利用40 47 类似的方法去重

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, idx, cur_ls, res):
        res.append(cur_ls[:])
        for i in range(idx, len(nums)):
            if i!=idx and nums[i]==nums[i-1]:
                continue
            cur_ls.append(nums[i])
            self.dfs(nums, i + 1, cur_ls, res)
            cur_ls.pop()
        # res.append(cur_ls[:])