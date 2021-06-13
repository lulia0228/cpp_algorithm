#
#
# @param matrix int整型二维数组
# @param target int整型
# @return bool布尔型
#

class Solution:
    def searchMatrix(self, matrix, target):
        # write code here
        m = len(matrix)
        n = len(matrix[0])
        lt, rt = 0, n - 1
        line = 0
        for i in range(m - 1, -1, -1):
            if target == matrix[i][0]:
                return True
            elif target > matrix[i][0]:
                line = i
                break
        while lt <= rt:
            mid = lt + (rt - lt) // 2
            if matrix[line][mid] == target:
                return True
            elif matrix[line][mid] > target:
                rt = mid - 1
            else:
                lt = mid + 1
        return False

