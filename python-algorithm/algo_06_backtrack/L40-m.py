#--coding:utf-8--
'''
@Time   : 2019/8/24
@Author : Heng Li
@Email  : liheng_lulia@163.com
'''

# 必须要先排序

class Solution:
    def __init__(self, **kwargs):
        self.res = []

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.dfs(candidates, 0, target, 0, [])
        return self.res

    def dfs(self, candidates, cur_sum, target, idx, cur_ls):
        if cur_sum == target:
            # 这里一开始直接append cur_ls，最后res成了[[],[]],是因为python参数传递的是引用，
            # 导致最后res里面的cur_ls也被更新掉了;a=[1,2,3]，b=a，a[0]=10则b相应变成【10，2，3】
            self.res.append(cur_ls[:])
            return
        # if cur_sum > target:
        #     return
        for i in range(idx, len(candidates)):
            # 剪枝
            if cur_sum > target:
                break
            if i != idx and candidates[i]==candidates[i-1]:
                continue
            cur_ls.append(candidates[i])
            # 因为每个数字在一个组合中只可以用1次，所以设置成i+1
            self.dfs(candidates, cur_sum + candidates[i], target, i+1, cur_ls)
            cur_ls.pop()