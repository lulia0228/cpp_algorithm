# -*- coding: utf-8 -*-
# @Time    : 2020/10/3 10:15
# @Author  : No Name

class Solution1:
    def myAtoi(self, str: str) -> int:
        import re
        mathes=re.match('[ ]*([+-]?\d+)',str)
        if not mathes:
            return 0
        ans=int(mathes.group(1))
        return min(max(ans,-2**31),2**31-1)

class Solution:
    def myAtoi(self, s: str) -> int:
        sz = len(s)
        idx = 0
        res = 0
        sign = 1
        while idx < sz and s[idx] == ' ':
            idx += 1
        if idx == sz:
            return 0
        if s[idx] == '-':
            sign = -1
        if s[idx] == '+' or s[idx] == '-':
            idx += 1
        while idx<sz and s[idx].isdigit():
            # 主要是为了模拟其它语言的32溢出问题，Python是64位整数
            if res > 2**31//10 or (res == 2**31//10 and int(s[idx])>7):
                return 2**31-1 if sign==1 else -2**31
            res = res*10 + int(s[idx])
            idx += 1
        return res if sign==1 else -res

p = Solution()
s1 = "words and 987"
s2 = " ++987"
s3 = " +987 3678888"
s4 = " -0000000120"
s5 = "   +"
print(p.myAtoi(s1))
print(p.myAtoi(s2))
print(p.myAtoi(s3))
print(p.myAtoi(s4))
print(p.myAtoi(s5))