#--coding:utf-8--

# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
# 例如：8 的平方根是 2.82842..., 返回2

# 终止条件和其它二分查找不太一样，取等了；边界更新也不一样

class Solution:

    def mySqrt(self, x: int) -> int:
        lt, rt, ans = 0, x, -1
        while lt <= rt:
            mid = lt+(rt-lt) // 2
            if mid * mid <= x:
                lt = mid + 1
            else:
                rt = mid - 1
        return lt-1


# 牛顿下降迭代；用y=x^2-C 斜率与0轴交点 逼近真实值
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        C, x0 = float(x), float(x)
        while True:
            xi = 0.5 * (x0 + C / x0)
            if abs(x0 - xi) < 1e-7:
                break
            x0 = xi

        return int(x0)
