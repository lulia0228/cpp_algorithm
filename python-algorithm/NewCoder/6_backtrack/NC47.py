#
#
# @param board char字符型二维数组
# @return void
#

# 写回溯要思考的三件事
# （1）回溯层数 （2）目标条件 （3）每层遍历的对象集合


class Solution:
    def __init__(self):
        self.row = [[False] * 10 for _ in range(9)]
        self.col = [[False] * 10 for _ in range(9)]
        self.box = [[False] * 10 for _ in range(9)]

    def solveSudoku(self, board):
        # write code here
        m = len(board)
        n = len(board[0])
        res = []
        objs = []
        for i in range(m):
            for j in range(n):
                if board[i][j] == '.':
                    objs.append([i, j])
                else:
                    self.row[i][int(board[i][j])] = True
                    self.col[j][int(board[i][j])] = True
                    self.box[(i // 3) * 3 + j // 3][int(board[i][j])] = True
        self.dfs(board, 0, [], objs, res)
        for i, n in enumerate(res[0]):
            board[objs[i][0]][objs[i][1]] = str(n)

        return

    def dfs(self, board, idx, tmp_ls, objs, res):
        if idx == len(objs):
            res.append(tmp_ls[:])
            return
        for i in range(1, 10):
            x, y = objs[idx]
            if not self.row[x][i] and not self.col[y][i] and not self.box[(x // 3) * 3 + y // 3][i]:
                tmp_ls.append(i)
                self.row[x][i] = True
                self.col[y][i] = True
                self.box[(x // 3) * 3 + y // 3][i] = True
                self.dfs(board, idx + 1, tmp_ls, objs, res)
                tmp_ls.pop()
                self.row[x][i] = False
                self.col[y][i] = False
                self.box[(x // 3) * 3 + y // 3][i] = False