#--coding:utf-8--

class Solution:
    def solve(self , M , N ):
        t = "0123456789ABCDEF"
        ans = ""
        if M == 0:
            return "0"
        fu = False
        if M < 0:
            fu = True
            M = -M
        while M!=0:
            ans = ans+t[M%N]
            M = M//N;

        #如果是负数，换成正数计算，最后再加上符号位
        if fu:
            ans = ans+"-"
        return ans[::-1]


res = Solution().solve(pow(2,31)-1, 16)
print(res)

# 0x80000000
# 0x7FFFFFFF

