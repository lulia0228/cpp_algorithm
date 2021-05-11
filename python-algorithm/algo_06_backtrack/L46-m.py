#--coding:utf-8--


class Solution:
    def __init__(self, **kwargs):
        self.res = []
        self.flag = []


    def permute(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return self.res
        self.flag = [False for i in range(len(nums))]
        self.dfs(nums, 0, [])
        return self.res

    def dfs(self, candinates, idx, cur_ls):
        if idx == len(candinates):
            self.res.append(cur_ls[:])
            return
        for i in range(len(candinates)):
            if not self.flag[i]:
                cur_ls.append(candinates[i])
                self.flag[i] = True
                self.dfs(candinates, idx + 1, cur_ls)
                cur_ls.pop()
                self.flag[i] = False



