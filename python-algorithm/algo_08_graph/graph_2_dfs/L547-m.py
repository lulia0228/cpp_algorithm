#--coding:utf-8--


# 计算图中有几个连通子图

# 1 DFS
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        res = 0
        m = len(isConnected)
        if m == 0: return res;
        # 标记第i个城市生是否已经被访问了
        visited = [False for i in range(m)]
        for i in range(m):
            if not visited[i]:
                res += 1
                self.dfs(isConnected, visited, i)
        return res

    def dfs(self, matrix, visited, i):
        for j in range(len(matrix)):
            if matrix[i][j] == 1 and not visited[j]:
                visited[j] = True
                self.dfs(matrix, visited, j)

# 2 BFS
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = len(isConnected)
        visited = set()
        circles = 0

        for i in range(provinces):
            if i not in visited:
                Q = collections.deque([i])
                while Q:
                    j = Q.popleft()
                    visited.add(j)
                    for k in range(provinces):
                        if isConnected[j][k] == 1 and k not in visited:
                            Q.append(k)
                circles += 1

        return circles


# 3 并查集