# -*- coding: utf-8 -*-
# 完全平方数的因数个数是奇数个，所以会被操作奇数次，那么最终会亮着
class Solution:
    def bulbSwitch(self, n: int) -> int:
        if n==1: return 1
        result = 1
        while True:
            if result*result>n:
                break
            result += 1
        return result-1

class Solution1:
    def bulbSwitch(self, n: int) -> int:
        return int(sqrt(n))