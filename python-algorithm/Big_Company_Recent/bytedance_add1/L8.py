# -*- coding: utf-8 -*-
INT_MAX=2**31-1
INT_MIN=-2**31


# 方法一
class Solution:
    def myAtoi(self, str: str) -> int:
        import re
        mathes=re.match('[ ]*([+-]?\d+)',str)
        if not mathes:
            return 0
        ans=int(mathes.group(1))
        return min(max(ans,-2**31),2**31-1)


# 方法二
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