# -*- coding: utf-8 -*-

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

# 有限状态机
INT_MAX=2**31-1
INT_MIN=-2**31

class Automata:
    def __init__(self):
        self.state="start"
        self.ans=0
        self.sign=1
        self.table={
            "start":["start","sign","innum","end"],
            "sign":["end","end","innum","end"],
            "innum":["end","end","innum","end"],
            "end":["end","end","end","end"],
        }
    def get_s(self,c):
        if c.isspace():
            return 0
        if c=='+' or c=='-':
            return 1
        if c.isdigit():
            return 2
        return 3

    def get(self,c):
        self.state=self.table[self.state][self.get_s(c)]
        if self.state=="innum":
            self.ans=self.ans*10+int(c)
            self.ans= min(self.ans,INT_MAX) if self.sign==1 else min(self.ans,-INT_MIN)
        if self.state=="sign":
            if c=='-':
                self.sign=-1


class Solution:
    def myAtoi(self, str: str) -> int:
        Auto=Automata()
        for c in str:
            Auto.get(c)
        return Auto.ans*Auto.sign

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