#--coding:utf-8--

# 必须要先排序
from typing import *
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        self.dfs(candidates, 0, target, [], res)
        return res

    def dfs(self, nums, idx, target, tmp, res):
        if target==0:
            res.append(tmp[:])
            return
        for i in range(idx, len(nums)):
            # 因为从小到大排序了，这里可以剪枝
            if target-nums[i]<0:
                break
            if i!=idx and nums[i]==nums[i-1]:
                continue
            tmp.append(nums[i])
            # 因为每个数字在一个组合中只可以用1次，所以设置成i+1
            self.dfs(nums, i+1, target-nums[i], tmp, res)
            tmp.pop()


class Solution:
    # res = [] # 直接这么写，在不停调用的情况下是不对的，因为所有案例的结果都会累加到res里

    def __init__(self, **kwargs):
        self.res = []

    def combinationSum2(self, candidates, target: int):
        candidates.sort()
        self.dfs(candidates, 0, target, 0, [])
        return self.res

    def dfs(self, candidates, cur_sum, target, idx, cur_ls):
        if cur_sum == target:
            self.res.append(cur_ls[:])
            return
        for i in range(idx, len(candidates)):
            if cur_sum + candidates[i] > target:
                break
            if i != idx and candidates[i] == candidates[i - 1]:
                continue
            cur_ls.append(candidates[i])
            self.dfs(candidates, cur_sum + candidates[i], target, i + 1, cur_ls)
            cur_ls.pop()

if __name__ == "__main__":
    num = [4,2,1,3,5,3,2]
    res = Solution().combinationSum2(num, 5)
    print(res)