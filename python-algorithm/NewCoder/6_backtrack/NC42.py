#
#
# @param num int整型一维数组
# @return int整型二维数组
#


class Solution:
    def permuteUnique(self, num):
        # write code here
        res = []
        if not num: return res
        visited = [False for _ in range(len(num))]
        num.sort()  # 排序必不可少
        self.dfs(num, 0, [], visited, res)
        return res

    def dfs(self, nums, idx, tmp_ls, visited, res):
        if idx == len(nums):
            res.append(tmp_ls[:])
            return
        for i in range(len(nums)):
            # 以下条件，必须结合排序使用
            if i != 0 and nums[i - 1] == nums[i] and not visited[i - 1]:
                continue
            if not visited[i]:
                visited[i] = True
                tmp_ls.append(nums[i])
                self.dfs(nums, idx + 1, tmp_ls, visited, res)
                tmp_ls.pop()
                visited[i] = False

