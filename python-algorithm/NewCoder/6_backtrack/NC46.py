#
#
# @param num int整型一维数组
# @param target int整型
# @return int整型二维数组
#

# 同 lc 40
class Solution:
    def combinationSum2(self, num, target):
        # write code here
        res = []
        #         visited = [False for _ in range(len(num))]
        num.sort()
        self.dfs(num, 0, target, [], res)
        return res

    def dfs(self, nums, idx, target, tmp_ls, res):
        if target < 0: return
        if target == 0:
            res.append(tmp_ls[:])
            return
        for i in range(idx, len(nums)):
            # 条件是i!=idx而不是i>0;即i不是当前组合的起始元素(避免 10 10 60 被去掉/ 避免 第2个 10 20 50的出现)
            if i != idx and nums[i - 1] == nums[i]: continue
            tmp_ls.append(nums[i])
            self.dfs(nums, i + 1, target - nums[i], tmp_ls, res)
            tmp_ls.pop()

