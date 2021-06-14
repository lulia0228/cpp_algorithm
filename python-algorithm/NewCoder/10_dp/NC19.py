# -*- coding: utf-8 -*-

class Solution:
    def maxsumofSubarray(self , arr ):
        # write code here
        final_max = arr[0]
        tmp_max = arr[0]
        for i in range(1, len(arr)):
            tmp_max = max(tmp_max+arr[i], arr[i])
            final_max = max(final_max, tmp_max)
        return final_max

