# -*- coding: utf-8 -*-

# 可以转换成435题  删除最少的区间 使剩下的区间互不重叠
# 此外，[1, 2] 和 [2, 3] 在本题中算是重叠区间

# 本题返回的是最终剩余不重叠区间的个数

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        sz = len(points)
        if sz == 0:
            return 0
        points.sort(key = lambda x:x[1])
        ref = points[0][1]
        cnt = 0
        for i in range(1, sz):
            if points[i][0] <= ref:
                cnt += 1
            else:
                ref = points[i][1]
        return sz-cnt
