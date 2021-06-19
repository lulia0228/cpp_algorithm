# -*- coding: utf-8 -*-
class Solution:
    def solve(self , A , B ):
        # write code here
        if len(A) != len(B):
            return False
        if A in B+B:
            return True
        return False