# -*- coding: utf-8 -*-
# @Time    : 2020/10/7 16:57
# @Author  : No Name

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
        m, n = 0, 0
        cnt = 0
        while m < len(g) and n < len(s):
            if g[m] <= s[n]:
                cnt += 1
                m += 1
                n += 1
            else:
                m += 1
        return cnt