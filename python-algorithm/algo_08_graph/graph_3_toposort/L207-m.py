#--coding:utf-8--
'''
@Time   : 2020/9/11
@Author : Heng Li
@Email  : liheng_lulia@163.com
'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = [[] for i in range(numCourses)]
        for connect in prerequisites:
            graph[connect[1]].append(connect[0])
        visited = [0 for i in range(numCourses)]
        for i in range(numCourses):
            if self.dfs(graph, i, visited):
                return False
        return True

    def dfs(self, graph, idx, visited):
        if visited[idx] == -1:  # 提前剪枝
            return False
        if visited[idx] == 1:
            return True
        visited[idx] = 1
        for nex in graph[idx]:
            if self.dfs(graph, nex, visited):
                return True
        visited[idx] = -1  # 说明以index为起始点的遍历无环
        return False
