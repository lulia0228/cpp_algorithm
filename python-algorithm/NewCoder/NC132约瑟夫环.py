#--coding:utf-8--
# f(n, m)表示长度为n的序列，删除n-1次，最后留下元素的序号
# f(n, m) = (f(n-1, m) + m) % n
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

class Solution:
    def ysf(self, n, m):
        # write code here
        if m < 1 or n < 1:
            return -1
        last = 0
        # i代表有目前有个人
        # 最后一轮剩下2个人，所以从2开始反推
        for i in range(2, n+1):
            last = (last + m) % i
        return last+1