#--coding:utf-8--
'''
@Time   : 2019/8/24
@Author : Heng Li
@Email  : liheng_lulia@163.com
'''

# 组合总数，结果不能重复（不考虑顺序）

class Solution:
    def __init__(self, **kwargs):
        self.res = []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.dfs(candidates, 0, target, 0, [])
        return self.res

    def dfs(self, candidates, cur_sum, target, idx, cur_ls):
        if cur_sum == target:
            # 这里一开始直接append cur_ls，最后res成了[[],[]],是因为python参数传递的是引用，
            # 导致最后res里面的cur_ls也被更新掉了;a=[1,2,3]，b=a，a[0]=10则b相应变成【10，2，3】
            self.res.append(cur_ls[:])
            return
        if cur_sum > target:
            return
        for i in range(idx, len(candidates)):
            cur_ls.append(candidates[i])
            self.dfs(candidates, cur_sum + candidates[i], target, i, cur_ls)
            cur_ls.pop()


# 优化
# 原题没说数组是有序的正整数数组,先排序，排序后可以剪枝
class Solution1:
    def __init__(self, **kwargs):
        self.res = []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.dfs(candidates, 0, target, 0, [])
        return self.res

    def dfs(self, candidates, cur_sum, target, idx, cur_ls):
        if cur_sum == target:
            # 这里一开始直接append cur_ls，最后res成了[[],[]],是因为python参数传递的是引用，
            # 导致最后res里面的cur_ls也被更新掉了;a=[1,2,3]，b=a，a[0]=10则b相应变成【10，2，3】
            self.res.append(cur_ls[:])
            return
        for i in range(idx, len(candidates)):
            # 剪枝
            if cur_sum > target:
                break
            cur_ls.append(candidates[i])
            self.dfs(candidates, cur_sum + candidates[i], target, i, cur_ls)
            cur_ls.pop()