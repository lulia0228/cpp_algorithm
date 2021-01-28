#--coding:utf-8--
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == []: return False
        m, n = len(matrix), len(matrix[0])
        lt, rt = m-1, 0
        while lt >= 0 and rt < n:
            if matrix[lt][rt] == target:
                return True
            elif matrix[lt][rt]>target:
                lt -= 1
            else:
                rt += 1
        return False
