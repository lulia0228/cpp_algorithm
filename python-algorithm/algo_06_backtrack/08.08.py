#--coding:utf-8--
class Solution:
    def permutation(self, S: str) -> List[str]:
        res = []
        if S == "": return res
        S = "".join(sorted(list(S)))
        visited = [False] * (len(S))
        self.dfs(S, "", res, visited)
        return res

    def dfs(self, S, tmp, res, visited):
        if len(tmp) == len(S):
            res.append(tmp)
        for i in range(len(S)):
            if i!=0 and S[i]==S[i-1] and visited[i-1]:
                continue
            if not visited[i]:
                visited[i] = True
                self.dfs(S, tmp + S[i], res, visited)
                visited[i] = False

