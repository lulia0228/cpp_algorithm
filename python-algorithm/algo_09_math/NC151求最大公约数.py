# -*- coding: utf-8 -*-
# class Solution:
#     def gcd(self , a , b ):
#         # write code here
#         for i in range(min(a,b),1, -1):
#             if a%i == 0  and b%i == 0:
#                 return i
#         return 1

class Solution:
    def gcd(self , a , b ):
        # write code here
        if a < b:
            a,b = b,a
        m = a%b # 下一次b到a的位置 m到b的位置
        while m:
            tmp = m
            m = b%m
            b = tmp
        return b

a,b = 60200240,492557950
# a,b = 8,12
res = Solution().gcd(a,b)
print(res)