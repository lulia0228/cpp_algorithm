#
#
# @param A int整型一维数组
# @param B int整型一维数组
# @return void
#

class Solution:
    def merge(self, A, m, B, n):
        # write code here
        p1, p2 = m - 1, n - 1
        p = m + n - 1
        while p1 >= 0 and p2 >= 0:
            if A[p1] > B[p2]:
                A[p] = A[p1]
                p1 -= 1
            else:
                A[p] = B[p2]
                p2 -= 1
            p -= 1
        # 不需要管第一个数组了，本身就是有序的
        while p2 >= 0:
            A[p] = B[p2]
            p -= 1
            p2 -= 1

