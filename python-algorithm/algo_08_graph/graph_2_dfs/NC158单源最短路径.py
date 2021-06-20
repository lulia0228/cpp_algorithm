# -*- coding: utf-8 -*-

import collections
class Solution:
    def findShortestPath(self, n, m, graph):
        # write code here
        def dfs(n, idx, path_sum, adj):
            if idx == n:
                self.ans = min(self.ans, path_sum)
                return
            for ed in adj[idx]:
                dfs(n, ed[0], path_sum + ed[1], adj)

        self.ans = float("inf")
        adj = collections.defaultdict(list)
        for edge in graph:
            if edge[1:] not in adj[edge[0]]:
                adj[edge[0]].append(edge[1:])
        dfs(n, 1, 0, adj)
        return self.ans

