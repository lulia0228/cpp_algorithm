# -*- coding: utf-8 -*-
# @Time    : 2020/10/6 22:52
# @Author  : No Name

class Solution:
    def canWinNim(self, n: int) -> bool:
        if n%4 == 0:
            return False
        return True