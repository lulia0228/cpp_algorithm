# -*- coding: utf-8 -*-


# 若为2的幂，则转为二进制必定有且仅有一个1，其他全为0；

# n&(n-1)可以去除二进制中最右边的 1
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0 :
            return False
        return (n&(n-1))==0

# n&（-n)可以得到二进制最右边的1
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        return n & (-n) == n