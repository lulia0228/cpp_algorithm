# -*- coding: utf-8 -*-
class Solution:
    def integerReplacement(self, n: int) -> int:
        Q = collections.deque()
        Q.append([n, 0])
        while Q:
            v, k = Q.popleft()
            if v == 1:
                return k
            elif v % 2 == 0:
                Q.append([v/2, k + 1])
            else:
                Q.append([(v - 1) , k + 1])
                Q.append([(v + 1) , k + 1])
