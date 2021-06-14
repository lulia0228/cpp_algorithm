# -*- coding: utf-8 -*-

class Solution:
    def Permutation(self, ss):
        # write code here
        if ss == "": return []
        res = []
        visited = [False] * len(ss)
        self.dfs(ss, "", res, visited)
        return res

    def dfs(self, ss, tmp_str, res, visited):
        if len(tmp_str) == len(ss):
            res.append(tmp_str)
            return
        for i in range(len(ss)):
            if i > 0 and ss[i] == ss[i - 1] and not visited[i - 1]:
                continue
            if not visited[i]:
                visited[i] = True
                self.dfs(ss, tmp_str + ss[i], res, visited)
                visited[i] = False