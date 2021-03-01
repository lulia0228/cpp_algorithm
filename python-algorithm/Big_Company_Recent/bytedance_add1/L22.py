# -*- coding: utf-8 -*-

# 参考组合排列类问题的回溯写法

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.dfs(n, 0, 0, '', res)
        return res

    def dfs(self, n, use_lt, use_rt, tmp, res):
        if use_lt == n and use_rt == n:
            res.append(tmp)
        if use_lt < use_rt:
            return
        if use_lt < n:
            self.dfs(n, use_lt+1, use_rt, tmp+'(', res)
        if use_rt < n:
            self.dfs(n, use_lt, use_rt+1, tmp+')', res)
# leetcode submit region end(Prohibit modification and deletion)