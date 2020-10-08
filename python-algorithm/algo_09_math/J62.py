# -*- coding: utf-8 -*-
# @Time    : 2020/10/6 22:59
# @Author  : No Name

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        record = [i for i in range(n)]
        idx = 0
        while len(record) > 1:
            idx = (idx+m-1)%len(record)
            record.pop(idx)
        return record[0]


# 快多了，但是没想明白怎么推出来的公式
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        p=0
        for i in range(2, n+1):
            p = (p+m)%i
        return p