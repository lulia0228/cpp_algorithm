# -*- coding: utf-8 -*-
# @Time    : 2020/10/6 13:21
# @Author  : No Name

# 乘法竖式，不会溢出，每次2个1位整数相乘
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        record = ['0' for i in range(m+n)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                tmp = int(record[i+j+1]) + int(num1[i])*int(num2[j])
                record[i+j+1] = str(tmp%10)
                record[i+j] = str(int(record[i+j])+tmp//10)
        for i in range(m+n):
            if record[i] != '0':
                return ''.join(record[i:])
        return '0'

# 直接存数字似乎快一些
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        record = [0 for i in range(m+n)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                tmp = record[i+j+1] + int(num1[i])*int(num2[j])
                record[i+j+1] = tmp%10
                record[i+j] = record[i+j]+tmp//10
        for i in range(m+n):
            if record[i] != 0:
                return ''.join([str(record[j])  for j in range(i, m+n)])
        return '0'