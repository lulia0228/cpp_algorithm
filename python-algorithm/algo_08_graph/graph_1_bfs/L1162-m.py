#--coding:utf-8--

class Solution:
    ori = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def maxDistance(self, grid: List[List[int]]) -> int:
        max_dis = -1
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    tmp = self.bfs(grid, i, j)
                    # print(i, j, tmp)
                    max_dis = max(max_dis, tmp)
        return max_dis

    def bfs(self, grid, x, y):
        m, n = len(grid), len(grid[0])
        vis = [[0] * n for i in range(m)]
        que = []
        que.append((x, y, 0))
        vis[x][y] = 1
        level = 0
        while que != []:
            sz = len(que)
            level += 1
            for i in range(sz):
                tmp_node = que.pop(0)
                # if tmp_node[2] == 1:
                #     return level-1
                for i in range(4):
                    new_x = tmp_node[0] + self.ori[i][0]
                    new_y = tmp_node[1] + self.ori[i][1]
                    if 0 <= new_x < m and 0 <= new_y < n and not vis[new_x][new_y]:
                        que.append((new_x, new_y, grid[new_x][new_y]))
                        vis[new_x][new_y] = 1
                        if grid[new_x][new_y] == 1:
                            return level
        return -1




