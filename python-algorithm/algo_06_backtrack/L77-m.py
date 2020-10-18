#--coding:utf-8--

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        if n <= 0 or k <= 0 or k > n:
            return res
        self.dfs(1, k, n, [], res)
        return res

    def dfs(self, idx, k, n, cur_ls, res):
        if len(cur_ls) == k:
            res.append(cur_ls[:])
            return
        for i in range(idx, n + 1):
            cur_ls.append(i)
            self.dfs(i + 1, k, n, cur_ls, res)
            cur_ls.pop()