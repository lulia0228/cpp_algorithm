#--coding:utf-8--
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 计算两个数之和
# @param s string字符串 表示第一个整数
# @param t string字符串 表示第二个整数
# @return string字符串
#

class Solution:
    def solve(self , s , t ):
        # write code here
        m, n = len(s), len(t)
        r_c = ["0"]*(max(m,n)+1)
        i , j, k = m-1, n-1, len(r_c)-1
        carry = 0
        while i >= 0 or j>=0:
            sum_ = 0
            if i>=0:
                sum_ += int(s[i])
                i -= 1
            if j>=0 :
                sum_ += int(t[j])
                j -= 1
            sum_ += carry
            r_c[k] = str(sum_%10)
            k -= 1
            carry = sum_//10
        if carry>0:
            r_c[k] = str(carry)
        if carry:
            return "".join(r_c)
        return "".join(r_c[1:])
