# -*- coding: utf-8 -*-
# @Time    : 2020/10/5 10:39
# @Author  : No Name

class Solution:
    def constructArray(self, n: int, k: int) :
        res = [1 for i in range(n)]
        i = 1
        interval = k
        while i <= k:
            if i%2 == 1:
                res[i] = res[i-1]+interval
            else:
                res[i] = res[i-1]-interval
            i += 1
            interval -= 1
        for i in range(k+1, n):
            res[i] = i+1
        return res

res = Solution().constructArray(10,5)
print(res)