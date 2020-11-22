# -*- coding: utf-8 -*-

# 自定义排序方式
from functools import cmp_to_key
class Solution:
    def minNumber(self, nums) -> str:
        def reversed_cmp(x, y):
            t1 = int(str(x) + str(y))
            t2 = int(str(y) + str(x))
            if t1 > t2:
                return 1
            if t1 < t2:
                return -1
            return 0
        s = sorted(nums, key=cmp_to_key(reversed_cmp))
        s = [str(i) for i in s]
        return "".join(s)

ls = [10,2]
print(Solution().minNumber(ls))