#--coding:utf-8--
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m, n = len(a), len(b)
        sum_ = 0
        carry = 0
        res = ""
        l1, l2 = -1, -1
        while l1 >= -m or l2 >= -n:
            if l1 >= -m:
                sum_ += int(a[l1])
                l1 -= 1
            if l2 >= -n:
                sum_ += int(b[l2])
                l2 -= 1
            sum_ += carry
            res = str(sum_%2) + res
            carry = sum_ // 2
            sum_ = 0
        if carry:
            res = str(1) + res
        return res