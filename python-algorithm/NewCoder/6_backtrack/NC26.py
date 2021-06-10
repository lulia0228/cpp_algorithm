#
#
# @param n int整型
# @return string字符串一维数组
#

# 回溯类的题目要善于设计辅助变量，帮助记录东西，例如本题的左右括号使用个数


class Solution:
    def generateParenthesis(self, n):
        # write code here
        res = []
        if n == 0: return res
        self.dfs(n, 0, 0, "", res)
        return res

    def dfs(self, n, use_lt, use_rt, tmp_s, res):
        if use_lt == n and use_rt == n:
            res.append(tmp_s)
            return
        if use_rt > use_lt: return
        if use_lt < n:
            self.dfs(n, use_lt + 1, use_rt, tmp_s + "(", res)
        if use_rt < n:
            self.dfs(n, use_lt, use_rt + 1, tmp_s + ")", res)

