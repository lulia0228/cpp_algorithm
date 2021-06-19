# -*- coding: utf-8 -*-

class Solution:
    def solve(self , s , t ):
        # write code here
        s1, s2 = len(s), len(t)
        r_d = [0]*(s1+s2)
        for i in range(-1, -1-s1, -1):
            for j in range(-1, -1-s2, -1):
                sum_ = r_d[i+j+1]
                sum_ += int(s[i])*int(t[j])
                r_d[i+j+1] = sum_%10
                r_d[i+j] += sum_//10
        if r_d[0] == 0:
            return "".join([str(item) for item in r_d[1:]])
        return "".join([str(item) for item in r_d])

s,t = "11","99"
res = Solution().solve(s,t)
print(res)