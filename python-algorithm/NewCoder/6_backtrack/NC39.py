#
#
# @param n int整型 the n
# @return int整型
#
class Solution:
    def __init__(self):
        self.col = []
        self.diag_1 = []
        self.diag_2 = []

    def Nqueen(self, n):
        # write code here
        res = []  # res存储的是每行的列索引
        self.col = [False] * n
        self.diag_1 = [False] * (2 * n - 1)
        self.diag_2 = [False] * (2 * n - 1)
        self.dfs(n, 0, [], res)

        return len(res)

    def dfs(self, n, row_idx, tmp_ls, res):
        if len(tmp_ls) == n:
            res.append(tmp_ls[:])
            return
        for c_idx in range(n):
            if not self.col[c_idx] and not self.diag_1[row_idx + c_idx] \
                    and not self.diag_2[row_idx - c_idx + n - 1]:
                tmp_ls.append(c_idx)
                self.col[c_idx] = True
                self.diag_1[row_idx + c_idx] = True
                self.diag_2[row_idx - c_idx + n - 1] = True
                self.dfs(n, row_idx + 1, tmp_ls, res)
                tmp_ls.pop()
                self.col[c_idx] = False
                self.diag_1[row_idx + c_idx] = False
                self.diag_2[row_idx - c_idx + n - 1] = False
