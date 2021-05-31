#--coding:utf-8--

class Solution:
    def permutation(self, S: str) -> List[str]:
        res = []
        if S == "": return res
        visited = [False]*(len(S))
        self.dfs(S, "", res, visited )
        return res

    def dfs(self, S, tmp, res, visited):
        if len(tmp) == len(S):
            res.append(tmp)
        for i in range(len(S)):
            if not visited[i]:
                visited[i] = True
                self.dfs(S, tmp+S[i], res, visited)
                visited[i] = False



