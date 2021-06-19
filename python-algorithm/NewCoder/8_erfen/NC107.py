#
# 寻找最后的山峰
# @param a int整型一维数组
# @return int整型
#
#


# 倒着分析，lc162是正向分析
# lc162只是找到其中一个，可以用二分，这里好像永不了二分法

class Solution:
    def solve(self, a):
        for i in range(len(a) - 1, 0, -1):
            if a[i] >= a[i - 1]:
                return i
