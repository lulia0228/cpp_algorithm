#
#
# @param n int整型
# @param m int整型
# @return int整型
#


# 模拟法
class Solution:
    def ysf(self, n, m):
        # write code here
        res = []
        for i in range(0, n):
            res.append(i + 1)
        i = 0
        for j in range(0, n - 1):
            i = (i + m - 1) % (n - j)
            res.pop(i)
        return res[0]


# 数学法没太懂
# f(n, m)表示长度为n的序列，删除n-1次，最后留下元素的序号
# f(n, m) = (f(n-1, m) + m) % n
class Solution1:
    def ysf(self , n , m ):
        # write code here
        p=0
        for i in range(2, n+1):
            p = (p+m)%i
        return p+1