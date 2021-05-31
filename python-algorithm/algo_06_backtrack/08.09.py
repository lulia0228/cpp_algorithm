#--coding:utf-8--

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0: return []
        res = []
        self.dfs(n, n, "", res)
        return res

    def dfs(self, lt_leave, rt_leave, tmp, res):
        if lt_leave == 0 and rt_leave == 0:
            res.append(tmp)
            return
        if lt_leave > rt_leave:
            return
        if lt_leave > 0:
            self.dfs(lt_leave-1, rt_leave, tmp+"(", res)
        if rt_leave > 0:
            self.dfs(lt_leave, rt_leave-1, tmp+")", res)

