# -*- coding: utf-8 -*-

import functools
class Solution:
    def minString(self , strs ):
        # write code here
        def my_sort(s1, s2):
            if s1+s2>s2+s1:
                return 1
            else:
                return -1
        strs.sort(key = functools.cmp_to_key(my_sort))
        return "".join(strs)