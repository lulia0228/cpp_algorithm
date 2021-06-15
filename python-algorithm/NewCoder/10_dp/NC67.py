#--coding:utf-8--

# 递归的经典
class Solution:
    def getSolution(self, n):
        # write code here
        s = []
        rst = self.get_rst(n, s, 'left', 'mid', 'right')
        return rst

    def get_rst(self, n, s, left, mid, right):
        if n == 1:
            s.append("move from " + left + " to " + right)
            return s
        else:
            self.get_rst(n - 1, s, left, right, mid)  # 将n-1个盘子从left借助right移动到mid上
            s.append("move from " + left + " to " + right)  # 将第n个盘子从left移动到right上
            self.get_rst(n - 1, s, mid, left, right)  # 将n-1个盘子从mid借助left移动到right上
            return s

res = Solution().getSolution(4)
print(res)