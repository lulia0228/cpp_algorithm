#--coding:utf-8--
# class Solution:
#     def pathWithObstacles(self, obstacleGrid: List[List[int]]) -> List[List[int]]:
#         if obstacleGrid[0][0] == 1:
#             return []
#         m, n = len(obstacleGrid), len(obstacleGrid[0])
#         res = []
#         visited = [[False]*n for i in range(m)]
#         self.dfs(obstacleGrid, 0, 0, [], res, visited)
#         if res == []:
#             return []
#         else:
#             return [[0,0]]+res[0]
#
#     def dfs(self, obstacleGrid, x, y, tmp, res, visited):
#
#         if x == len(obstacleGrid)-1 and y == len(obstacleGrid[0])-1:
#             res.append(tmp[:])
#             return
#         #  不加visited就超时
#         if not visited[x][y]:
#             visited[x][y] = True
#             for ori in [[0,1],[1,0]]:
#                 new_x = x + ori[0]
#                 new_y = y + ori[1]
#                 if new_x < len(obstacleGrid) and new_y < len(obstacleGrid[0]) \
#                                                and obstacleGrid[new_x][new_y] == 0:
#                         tmp.append([new_x, new_y])
#                         self.dfs(obstacleGrid, new_x, new_y, tmp, res, visited)
#                         tmp.pop(-1)


class Solution:
    def pathWithObstacles(self, obstacleGrid: List[List[int]]) -> List[List[int]]:
        if obstacleGrid[0][0] == 1:
            return []
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        res = []
        visited = [[False]*n for i in range(m)]
        self.dfs(obstacleGrid, 0, 0, [], res, visited)
        if res == []:
            return []
        else:
            return res[0]+[[m-1, n-1]]

    def dfs(self, obstacleGrid, x, y, tmp, res, visited):

        if x == len(obstacleGrid)-1 and y == len(obstacleGrid[0])-1 :
            if obstacleGrid[x][y] == 0:
                res.append(tmp[:])
            return
        #  不加visited就超时
        if not visited[x][y]:
            if obstacleGrid[x][y] == 0:
                visited[x][y] = True
                tmp.append([x, y])
                for ori in [[0,1],[1,0]]:
                    new_x = x + ori[0]
                    new_y = y + ori[1]
                    if new_x < len(obstacleGrid) and new_y < len(obstacleGrid[0]) :
                            self.dfs(obstacleGrid, new_x, new_y, tmp, res, visited)
                tmp.pop(-1)

# 关于dfs 回溯 中 append和pop的位置需要仔细想一想
