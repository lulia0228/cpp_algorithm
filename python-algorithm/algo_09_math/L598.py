# -*- coding: utf-8 -*-
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        x, y = m, n
        for op in ops:
            x = min(x, op[0])
            y = min(y, op[1])
        return x*y