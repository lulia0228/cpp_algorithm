#--coding:utf-8--
class Solution:
    def multiply(self, A: int, B: int) -> int:
        if B == 0:
            return 0
        sum_ = A + self.multiply(A, B-1)
        return sum_