#--coding:utf-8--
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        if nums == []: return  res
        visited = [False]*(len(nums))
        self.dfs(nums, 0, [], res, visited)
        return res

    def dfs(self, nums, idx, tmp, res, visited):
        res.append(tmp[:])
        for i in range(idx, len(nums)):
            if not visited[i]:
                visited[i] = True
                tmp.append(nums[i])
                self.dfs(nums, i+1, tmp, res, visited)
                tmp.pop(-1)
                visited[i] = False
