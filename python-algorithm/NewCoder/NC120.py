# -*- coding: utf-8 -*-

# python中，对于负数，无论是右移操作，还是n&（n-1）操作，都会陷入死循环。
# 所以利用上述这个小技巧，将负数的影响用于0xffffffff相与变为python认为的正数（与机器中的补码相同）。
# 然后利用正数来进行操作就简单了。
class Solution:
    def NumberOf1(self, n):
        # write code here
        cnt = 0
        if n < 0:
            n = n & 0xffffffff
        while n:
            n = n&(n-1)
            cnt += 1
        return cnt