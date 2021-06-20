# -*- coding: utf-8 -*-

class Solution:
    def minmumNumberOfHost(self , n , startEnd ):
        # write code here
        start=[x[0] for x in startEnd]
        end=[x[1] for x in startEnd]
        start.sort()
        end.sort()
        count,j=0,0
        for i in range(n):
            if start[i]>=end[j]: j+=1
            else: count+=1
        return count

