#--coding:utf-8--

import collections
class Solution:
    def topKstrings(self , strings , n ):
        # write code here
        r_d = collections.defaultdict(int)
        for ss in strings:
            r_d[ss] += 1
        r = sorted(r_d.items(), key = lambda x: (-x[1], x[0]))
        return r[:n]

