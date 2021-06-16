
class Interval:
    def __init__(self, a=0, b=0):
        self.start = a
        self.end = b


class Solution:
    def merge(self, intervals):
        # write code here
        res = []
        if not intervals: return res
        intervals = sorted(intervals, key=lambda x: (x.start, x.end))
        res.append(intervals[0])
        for i in range(1, len(intervals)):
            if intervals[i].start <= res[-1].end:
                # 上一个区间的末尾可能大于当前区间的末尾
                res[-1].end = max(res[-1].end, intervals[i].end)
            else:
                res.append(Interval(intervals[i].start, intervals[i].end))
        return res
