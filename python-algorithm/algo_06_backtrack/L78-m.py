#--coding:utf-8--

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(0, nums, [], res)
        return res

    def dfs(self, idx, nums, tmp, res):
        # res.append(tmp[:])
        for i in range(idx, len(nums)):
            tmp.append(nums[i])
            # 是i+1从下一个位置开始
            self.dfs(i + 1, nums, tmp, res)
            tmp.pop()
        # 放在前面和后面的顺序不一样
        res.append(tmp[:])
