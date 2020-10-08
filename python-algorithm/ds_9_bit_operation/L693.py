# -*- coding: utf-8 -*-
# @Time    : 2020/10/7 12:50
# @Author  : No Name

# 对于 1010 这种位级表示的数，把它向右移动 1 位得到 101，这两个数每个位都不同，因此异或得到的结果为 1111。

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        a = n^(n>>1)
        return a&(a+1) == 0