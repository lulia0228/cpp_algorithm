#--coding:utf-8--
'''
@Time   : 2020/9/10
@Author : Heng Li
@Email  : liheng_lulia@163.com
'''


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        res = 0
        m = len(M)
        if (m == 0):
            return res;
        # 标记第i个学生是否已经被访问了
        visited = [False for i in range(m)]
        for i in range(m):
            if not visited[i]:
                res += 1
                self.dfs(M, visited, i)
        return res

    def dfs(self, matrix, visited, i):
        for j in range(len(matrix)):
            if matrix[i][j] == 1 and not visited[j]:
                visited[j] = True
                self.dfs(matrix, visited, j)
