#--coding:utf-8--

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visit = [False] * len(nums)
        self.dfs(nums, visit, [], res)
        return res

    def dfs(self, nums, visit, tmp, res):
        if len(tmp) == len(nums):
            res.append(tmp[:])
            return
        for i in range(len(nums)):
            if not visit[i]:
                visit[i] = True
                tmp.append(nums[i])
                self.dfs(nums, visit, tmp, res)
                visit[i] = False
                tmp.pop()





