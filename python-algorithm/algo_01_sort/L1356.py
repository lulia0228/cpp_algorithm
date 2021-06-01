#--coding:utf-8--

from functools import cmp_to_key
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:

        def nums_of_bit1(num):
            cnt = 0
            while num:
                if num&1 :
                    cnt += 1
                num >>= 1
            return cnt

        def comp(x,y):
            if nums_of_bit1(x) > nums_of_bit1(y):
                return 1
            elif nums_of_bit1(x) < nums_of_bit1(y):
                return -1
            elif nums_of_bit1(x) == nums_of_bit1(y):
                if x > y:
                    return 1
                elif x < y:
                    return -1
            return 0

        res = sorted(arr, key=cmp_to_key(comp))

        return res