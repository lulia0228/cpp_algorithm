#--coding:utf-8--

# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
# 例如：8 的平方根是 2.82842..., 返回2

# 终止条件和其它二分查找不太一样，取等了；边界更新也不一样

class Solution:

    def mySqrt(self, x: int) -> int:
        l, r, ans = 0, x, -1
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans