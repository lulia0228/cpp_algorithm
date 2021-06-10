
#
#
# @param A int整型一维数组
# @return int整型二维数组
#

# 无重复元素数组的所有子集

class Solution:
    def subsets(self, A):
        # write code here
        res = []
        if not A: return res
        A.sort()
        self.dfs(A, 0, [], res)
        return res

    def dfs(self, nums, idx, tmp_ls, res):
        res.append(tmp_ls[:])
        for i in range(idx, len(nums)):
            tmp_ls.append(nums[i])
            self.dfs(nums, i + 1, tmp_ls, res)
            tmp_ls.pop()