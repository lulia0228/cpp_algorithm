#--coding:utf-8--

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # 特殊情况处理
        if int(num1) == 0 or int(num2)==0:
            return "0"
        n1, n2 = len(num1), len(num2)
        record = [0]*(n1+n2+2)
        for i in range(-1, -1-n1, -1):
            for j in range(-1, -1-n2, -1):
                t_sum = record[i+j+1]+int(num1[i])*int(num2[j])
                record[i+j+1] = t_sum%10
                record[i+j] += t_sum//10
        idx = 0
        while record[idx] == 0:
            idx += 1
        return "".join([str(i)  for i in record[idx:]])


