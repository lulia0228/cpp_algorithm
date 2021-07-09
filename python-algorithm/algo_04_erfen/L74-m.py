#--coding:utf-8--

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        row = 0
        for i in range(m-1, -1, -1):
            if target>=matrix[i][0]:
                row = i
                break # 容易漏掉
        lt, rt = 0, n-1
        while lt<=rt:
            mid = lt +(rt-lt)//2
            if matrix[row][mid]==target:
                return True
            elif matrix[row][mid]>target:
                rt = mid-1
            else:
                lt = mid+1
        return False