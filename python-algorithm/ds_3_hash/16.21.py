#--coding:utf-8--
class Solution:
    def findSwapValues(self, array1: List[int], array2: List[int]) -> List[int]:
        sum1, sum2 = sum(array1), sum(array2)
        if abs(sum1-sum2)%2 != 0:
            return []
        st = set(array2)
        for item in array1:
            tmp = item-(sum1-sum2)//2
            if  tmp in st:
                return [item, tmp]
        return []