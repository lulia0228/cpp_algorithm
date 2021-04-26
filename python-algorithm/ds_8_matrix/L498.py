#--coding:utf-8--
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        reserve = [[] for i in range(m+n-1)]
        for i in range(m):
            for j in range(n):
                reserve[i+j].append(mat[i][j])
        res = []
        for idx, diag in enumerate(reserve):
            if idx%2 == 0:
                res.extend(diag[::-1])
            else:
                res.extend(diag)
        return res
