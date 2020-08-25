#--coding:utf-8--
'''
@Time   : 2020/8/25
@Author : Heng Li
@Email  : liheng_lulia@163.com
'''

class Solution:
    def __init__(self, **kwargs):
        self.row = []
        self.col = []
        self.box = []
        self.blank = []
        self.res = []

    # def solveSudoku(self, board: List[List[str]]) -> None:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 里面做成10是为了映射到1-9具体每个数字
        # 记录每行每个数是否出现过；每列...;每个九宫格...
        self.row = [[0 for j in range(10)] for i in range(9)]
        self.col = [[0 for j in range(10)] for i in range(9)]
        self.box = [[0 for j in range(10)] for i in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    self.blank.append([i,j])
                else:
                    curNum = int(board[i][j])
                    self.row[i][curNum] = 1
                    self.col[j][curNum] = 1
                    self.box[j//3+(i//3)*3][curNum] = 1
        self.dfs(board, 0, [])
        # 题目说假设只有一种解，即res里面只含有一组解
        for i in range(len(self.res[0])):
            board[self.blank[i][0]][self.blank[i][1]] = str(self.res[0][i])

    def dfs(self, board, idx, cur_ls):
        if idx == len(self.blank):
            self.res.append(cur_ls[:])
            return
        for num in range(1,10):
            t_r = self.blank[idx][0]
            t_c = self.blank[idx][1]
            if not self.row[t_r][num] and not self.col[t_c][num] and \
            not self.box[t_c//3 + (t_r//3)*3][num]:
                cur_ls.append(num)
                self.row[t_r][num] = 1
                self.col[t_c][num] = 1
                self.box[t_c//3 + (t_r//3)*3][num] = 1
                self.dfs(board, idx+1, cur_ls)
                cur_ls.pop()
                self.row[t_r][num] = 0
                self.col[t_c][num] = 0
                self.box[t_c//3 + (t_r//3)*3][num] = 0


if __name__ == "__main__":
    board =[['5','3','.','.','7','.','.','.','.'],
            ['6','.','.','1','9','5','.','.','.'],
            ['.','9','8','.','.','.','.','6','.'],
            ['8','.','.','.','6','.','.','.','3'],
            ['4','.','.','8','.','3','.','.','1'],
            ['7','.','.','.','2','.','.','.','6'],
            ['.','6','.','.','.','.','2','8','.'],
            ['.','.','.','4','1','9','.','.','5'],
            ['.','.','.','.','8','.','.','7','9']]

    Solution().solveSudoku(board)
    for i in board:
        print(i)