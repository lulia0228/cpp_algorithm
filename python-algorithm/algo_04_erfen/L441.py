# -*- coding: utf-8 -*-

from math import sqrt
class Solution:
    def arrangeCoins(self, n: int) -> int:
        lt, rt = 0, int(sqrt(2*n))
        while lt <= rt:
            mid = lt+(rt-lt)//2
            if mid*(mid+1) > 2*n:
                rt = mid - 1
            else:
                lt = mid + 1
        return lt-1

if __name__ == "__main__":
    print(Solution().arrangeCoins(3))