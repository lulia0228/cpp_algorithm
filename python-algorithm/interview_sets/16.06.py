#--coding:utf-8--
class Solution:
    def smallestDifference(self, a: List[int], b: List[int]) -> int:
        a.sort()
        b.sort()
        i, j, res = 0, 0, 2**32-1
        while i<len(a) and j<len(b):
            res = min(abs(a[i]-b[j]), res)
            if a[i]>b[j]: j += 1
            else: i += 1
        return res