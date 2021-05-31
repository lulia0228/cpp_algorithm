#--coding:utf-8--


class Solution:
    def __init__(self, **kwargs):
        self.col = []
        self.diag1 = []
        self.diag2 = []
        self.res = []

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.col = [False for i in range(n)]
        self.diag1 = [False for i in range(2*n-1)]
        self.diag2 = [False for i in range(2*n-1)]
        self.pushQueen(n, 0, [])
        return self.res

    def pushQueen(self, n, line_idx, cur_ls):
        if line_idx==n:
            self.res.append(self.generateBoard(n, cur_ls))
            return
        for col_idx in range(n):
            if not self.col[col_idx] and not self.diag1[line_idx+col_idx] and not \
            self.diag2[line_idx-col_idx+n-1]:
                cur_ls.append(col_idx)
                self.col[col_idx] = True
                self.diag1[line_idx+col_idx] = True
                self.diag2[line_idx-col_idx+n-1] = True
                self.pushQueen(n, line_idx+1, cur_ls)
                cur_ls.pop()
                self.col[col_idx] = False
                self.diag1[line_idx+col_idx] = False
                self.diag2[line_idx-col_idx+n-1] = False

    def generateBoard(self, n, row):
        ans = []
        for i in range(n):
            ans.append("".join(['Q' if j==row[i] else '.'for j in range(n)]))
        return ans
