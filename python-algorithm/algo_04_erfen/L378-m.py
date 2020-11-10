#--coding:utf-8--

# //这里的二分法，二分的不是索引，而是实际值，通过判断矩阵中<=mid的元素多少，来确定值的区间。

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        lt_val, rt_val = matrix[0][0], matrix[m - 1][n - 1]
        while lt_val < rt_val:
            mid = lt_val + (rt_val - lt_val) // 2
            cnt = self.findNotBiggerThanMid(matrix, m, n, mid)
            if cnt < k:
                lt_val = mid + 1
            else:
                rt_val = mid
        return lt_val

    def findNotBiggerThanMid(self, matrix, m, n, mid):
        i, j = m - 1, 0
        cnt = 0
        while i >= 0 and j < n:
            if matrix[i][j] <= mid:
                cnt += (i + 1)  # 前元素所在列的上方的元素全部都小于mid
                j += 1
            else:
                i -= 1
        return cnt



