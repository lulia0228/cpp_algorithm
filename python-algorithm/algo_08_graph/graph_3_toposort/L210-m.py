#--coding:utf-8--


# 1 拓扑排序
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = [] # res存储的就是能完成的顺序
        degree = [0 for _ in range(numCourses)]
        graph = [[] for _ in range(numCourses)]
        for p in prerequisites:
            graph[p[1]].append(p[0])
            degree[p[0]] += 1  # p[0]点入度加1
        q = collections.deque()
        # 将入度为0的节点全部加入队列
        for i in range(numCourses):
            if degree[i] == 0:
                q.append(i)
        while q:
            t = q.popleft()
            res.append(t)
            # 删除所有与当前节点相连的边
            for i in graph[t]:
                degree[i] -= 1
                # 度变成0的节点加入队列
                if degree[i] == 0:
                    q.append(i)
        if len(res) == numCourses:
            return res
        return []


# 2 DFS
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for i in range(numCourses)]
        for connect in prerequisites:
            graph[connect[1]].append(connect[0])
        visited = [0 for i in range(numCourses)]
        res = []
        for i in range(numCourses):
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