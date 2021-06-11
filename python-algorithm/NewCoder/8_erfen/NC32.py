#
#
# @param x int整型
# @return int整型
#

class Solution:
    def sqrt(self, x):
        # write code here
        if x == 0: return 0
        if x < 4: return 1
        lt, rt = 2, x // 2
        while lt <= rt:
            mid = lt + (rt - lt) // 2
            if mid * mid > x:
                rt = mid - 1
            elif mid * mid < x:
                lt = mid + 1
            else:
                return mid
        return lt - 1
