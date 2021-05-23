# -*- coding: utf-8 -*-

class Solution(object):
    def partitionDisjoint(self, A):
        N = len(A)
        maxleft = [None] * N
        minright = [None] * N

        m = A[0]
        for i in range(N):
            m = max(m, A[i])
            maxleft[i] = m

        m = A[-1]
        for i in range(N-1, -1, -1):
            m = min(m, A[i])
            minright[i] = m

        for i in range(N-1):
            if maxleft[i] <= minright[i+1]:
                return i+1