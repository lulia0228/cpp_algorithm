#--coding:utf-8--
class Solution:
    def fib(self, n: int) -> int:
        if n < 2: return n
        a, b = 0, 1
        c = 0
        for _ in range(2, n+1):
            c = a + b
            a, b = b, a+b

        return c