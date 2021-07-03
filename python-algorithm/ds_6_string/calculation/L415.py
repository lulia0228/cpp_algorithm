#--coding:utf-8--

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        m, n = len(num1)-1, len(num2)-1
        res = ""
        carry = 0
        while m>=0 or n>=0:
            tmp_sum = 0
            if m>=0:
                tmp_sum += int(num1[m])
                m -= 1
            if n>=0:
                tmp_sum += int(num2[n])
                n -= 1
            tmp_sum += carry
            res = str(tmp_sum%10) + res
            carry = tmp_sum//10
        if carry:
            res = str(carry) + res
        return res