# -*- coding: utf-8 -*-
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        cnt_a, cnt_b, cnt_c = 0, 0, 0

        res = 0
        L = 0
        for R in range(n):
            if s[R] == 'a':     cnt_a += 1
            if s[R] == 'b':     cnt_b += 1
            if s[R] == 'c':     cnt_c += 1

            # while min(cnt_a, min(cnt_b, cnt_c ))>=1:
            # 速度更快
            while cnt_a>=1 and cnt_b>=1 and  cnt_c>=1:
                res += (n - R)                  #与右侧剩下的，可以组成合法的情况（R也是合理的）

                if s[L] == 'a':     cnt_a -= 1
                if s[L] == 'b':     cnt_b -= 1
                if s[L] == 'c':     cnt_c -= 1
                L += 1
        return res

