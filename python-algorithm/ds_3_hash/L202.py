#--coding:utf-8--
class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while n != 1 and n not in s:
            s.add(n)
            n = self.getSquareSum(n)
        return n==1

    def getSquareSum(self, n):
        res = 0
        while n :
            pop = n%10
            n = n//10
            res += pop*pop
        return res