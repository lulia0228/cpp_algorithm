#--coding:utf-8--

# 字符串相加
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sz1, sz2 = len(num1), len(num2)
        if sz1 > sz2:
            num2 = '0'*(sz1-sz2) + num2
        else:
            num1 = '0'*(sz2-sz1) + num1
        reserve = [0]*(max(sz1, sz2) + 1)
        for i in range(-1, -max(sz1, sz2)-1, -1):
            tmp_sum = int(num1[i])+int(num2[i])+reserve[i]
            reserve[i] = tmp_sum%10
            reserve[i-1] += tmp_sum//10

        res = "".join([str(i) for i in reserve])
        if res[0] == '0':
            res = res[1:]
        return res