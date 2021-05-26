#--coding:utf-8--


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if grid[0][0] == 1 or grid[m-1][n-1] == 1 or m==0:
            return -1
        if m == 1 :
            return 1
        orient = [[1, -1], [1, 0], [1, 1], [0, -1], [0, 1], \
                    [-1, -1], [-1, 0], [-1, 1]]
        que = []
        que.append((0,0))
        level = 0
        while que != []:
            cur_level_size = len(que)
            level += 1
            for s in range(cur_level_size):
                cur_node = que.pop(0)
                tmp_x = cur_node[0]
                tmp_y = cur_node[1]
                # 处理的是1x1的0矩阵的特殊情况，可以在上面if m==1 处给单独处理
                # if tmp_x == m-1 and tmp_y == n-1:
                #     return level
                for i in range(8):
                    new_x = tmp_x+orient[i][0]
                    new_y = tmp_y+orient[i][1]
                    if new_x == m-1 and new_y == n-1:
                        return level+1
                    if new_x>=0 and new_x<m and new_y>=0 and \
                     new_y<n and grid[new_x][new_y] == 0:
                        que.append((new_x, new_y))
                        # 改了值，相当于标记这个节点已经被访问了，不用额外设置一个visited数组
                        grid[new_x][new_y] = 1
        return -1
