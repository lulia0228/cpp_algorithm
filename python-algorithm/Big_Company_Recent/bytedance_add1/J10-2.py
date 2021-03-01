# -*- coding: utf-8 -*-
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numWays(self, n: int) -> int:
        if n == 0: return 1
        if n < 3: return n
        a, b = 1, 2
        c = 0
        for i in range(3,n+1):
            c = a + b
            a, b = b, c
        return c%(1000000007)
# leetcode submit region end(Prohibit modification and deletion)