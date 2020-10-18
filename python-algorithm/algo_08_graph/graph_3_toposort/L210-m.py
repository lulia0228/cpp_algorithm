#--coding:utf-8--


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for i in range(numCourses)]
        for connect in prerequisites:
            graph[connect[1]].append(connect[0])
        visited = [0 for i in range(numCourses)]
        res = []
        for i in range(numCourses):
            # True表示有环
            if self.dfs(graph, i, visited, res):
                return []
        return res[::-1] # 为什么要反序，思考下!

    def dfs(self, graph, idx, visited, res):
        if visited[idx] == -1:  # 提前剪枝
            return False
        if visited[idx] == 1:
            return True
        visited[idx] = 1
        for nex in graph[idx]:
            if self.dfs(graph, nex, visited, res):
                return True
        visited[idx] = -1  # 说明以index为起始点的遍历无环
        res.append(idx)
        return False