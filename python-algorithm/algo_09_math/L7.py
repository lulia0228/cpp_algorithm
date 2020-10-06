# -*- coding: utf-8 -*-
# @Time    : 2020/10/6 12:14
# @Author  : No Name

# 有2点要注意：
# 1 C、C++、java语言，这些是向0取值，-10对3取余得 -3 余 -1 ，而python是向负无穷取值，-10对3取余得 -4 余 2.
# 2 python语言本身不用担心整型32位溢出问题，但是这里对其它语言来说是考察点，所以要模拟出来
class Solution:
    def reverse(self, x: int) -> int:
        max32 = 2**31-1
        sign = 1
        if x < 0:
            sign = -1
        rev = 0
        tmp = abs(x)
        while tmp != 0:
            pop = tmp%10
            if rev > max32//10:
                return 0
            if rev == max32//10:
                if sign == 1 and pop>7:
                    return 0
                if sign == -1 and pop>8:
                    return 0
            rev = rev*10 + pop
            tmp = tmp//10
        return sign*rev

# 这种写法虽然没错误，但是中间值已经超过32位了，不符合题目考察点
class Solution:
    def reverse(self, x: int) -> int:
        max32 = 2**31-1
        sign = 1
        if x < 0:
            sign = -1
        rev = 0
        tmp = abs(x)
        while tmp != 0:
            pop = tmp%10
            rev = rev*10 + pop
            tmp = tmp//10
        res = sign*rev
        if res > 2**31-1 or res < -2**31:
            return 0
        return res