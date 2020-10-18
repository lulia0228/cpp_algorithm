# -*- coding: utf-8 -*-


# 本题返回的是：要删除的区间的个数
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sz = len(intervals)
        if sz == 0:
            return 0
        intervals.sort(key = lambda x:x[1])
        ref = intervals[0][1]
        cnt = 0
        for i in range(1, sz):
            if intervals[i][0]<ref:
                cnt += 1
            else:
                ref = intervals[i][1]
        return cnt
