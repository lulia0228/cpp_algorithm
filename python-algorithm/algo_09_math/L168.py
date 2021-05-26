#--coding:utf-8--

class Solution:
    def convertToTitle(self, n: int) -> str:
        s = ''
        while n:
            n -= 1 # 每次转化前需要-1,因为A 对应的是1不是0
            #ASCII码转大写字符 并且左加
            # print(65 + n % 26, chr(65 + n % 26))
            s = chr(65 + n % 26) + s
            n //= 26
        return s

print(Solution().convertToTitle(701))