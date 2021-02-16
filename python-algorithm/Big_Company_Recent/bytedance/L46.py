# -*- coding: utf-8 -*-

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sz = len(nums)
        if sz == 0: return []
        res = []
        visited = [0] * sz
        self.dfs(nums, [], visited, res)
        return res

    def dfs(self, nums, tmp, visited, res):
        if len(tmp) == len(nums):
            res.append(tmp[:])
            return
        for i in range(len(nums)):
            if not visited[i]:
                visited[i] = 1
                tmp.append(nums[i])
                self.dfs(nums, tmp, visited, res)
                tmp.pop(-1)
                visited[i] = 0
