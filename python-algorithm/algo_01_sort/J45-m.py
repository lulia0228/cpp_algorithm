#--coding:utf-8--
class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def cmp(x,y):
            s1, s2 = str(x)+str(y), str(y)+str(x)
            if int(s1)>int(s2):
                return 1
            elif int(s1)<int(s2):
                return -1
            else:
                return 0
        nums.sort(key = functools.cmp_to_key(cmp))
        return "".join([str(i) for i in nums])
