# -*- coding: utf-8 -*-
class Solution:
    def addDigits(self, num: int) -> int:
        def pending_num(num):
            sum = 0
            while num:
                sum += num % 10
                num //= 10
            return sum
        while num >= 10:
            num = pending_num(num)
        return num
