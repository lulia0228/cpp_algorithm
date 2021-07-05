# -*- coding: utf-8 -*-

# 有2点要注意：
# 1 C、C++、java语言，这些是向0取值，-10对3取余得 -3 余 -1 ，而python是向负无穷取值，-10对3取余得 -4 余 2.
# 2 python语言本身不用担心整型32位溢出问题，但是这里对其它语言来说是考察点，所以要模拟出来

class Solution:
    def reverse(self, x: int) -> int:
        m = x
        flag = 1
        if x < 0:
            m = -x
            flag = -1
        ans = 0
        while m:
            mod = m % 10
            if ans > pow(2, 31) // 10:
                return 0
            if ans == pow(2, 31) // 10:
                if (mod > 7 and flag == 1):
                    return 0
                if (mod > 8 and flag == -1):
                    return 0
            ans = ans * 10 + mod
            m //= 10

        return flag * ans

