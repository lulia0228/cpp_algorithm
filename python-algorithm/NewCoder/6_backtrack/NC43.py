#
#
# @param num int整型一维数组
# @return int整型二维数组
#

# 无重复元素数组的全排列

class Solution:
    def permute(self, num):
        # write code here
        res = []
        if not num: return res
        visited = [False for _ in range(len(num))]
        self.dfs(num, 0, [], visited, res)
        return res

    def dfs(self, nums, cnt, tmp_ls, visited, res):
        if cnt == len(nums):
            res.append(tmp_ls[:])
            return
        for i in range(len(nums)):
            if not visited[i]:
                visited[i] = True
                tmp_ls.append(nums[i])
                self.dfs(nums, cnt + 1, tmp_ls, visited, res)
                tmp_ls.pop()
                visited[i] = False
