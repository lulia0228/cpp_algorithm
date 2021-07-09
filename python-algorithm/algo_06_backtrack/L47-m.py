#--coding:utf-8--

# 必须要排序，否则没法用下面的办法去重
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        visited = [False]*(len(nums))
        res = []
        self.dfs(nums, visited, [], res)
        return res

    def dfs(self, nums, visited, tmp, res):
        if len(tmp) == len(nums):
            res.append(tmp[:])
            return
        for i in range(len(nums)):
            # 去重
            if i>0 and nums[i]==nums[i-1] and not visited[i-1]:
                continue
            if not visited[i]:
                visited[i] = True
                tmp.append(nums[i])
                self.dfs(nums, visited, tmp, res)
                visited[i] = False
                tmp.pop()

