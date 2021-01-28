#--coding:utf-8--

class StreamRank:

    def __init__(self):
        self.record = dict()

    def track(self, x: int) -> None:
        if x not in self.record:
            self.record[x] = 1
        else:
            self.record[x] += 1

    def getRankOfNumber(self, x: int) -> int:
        res = 0
        for k,v in self.record.items():
            if k<=x:
                res += self.record[k]
        return res


# Your StreamRank object will be instantiated and called as such:
# obj = StreamRank()
# obj.track(x)
# param_2 = obj.getRankOfNumber(x)