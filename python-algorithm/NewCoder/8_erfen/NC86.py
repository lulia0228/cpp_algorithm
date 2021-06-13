# -*- coding: utf-8 -*-

class Solution:
    def findElement(self, mat, n, m, x):
        # write code here
        lt, rt = 0, m-1
        while lt < n and rt >=0:
            if mat[lt][rt]>x:
                rt -= 1
            elif mat[lt][rt]<x:
                lt += 1
            else:
                return [lt, rt]
        return [-1, -1]