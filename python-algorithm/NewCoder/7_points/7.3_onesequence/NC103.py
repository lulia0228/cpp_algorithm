#
# 反转字符串
# @param str string字符串
# @return string字符串
#

class Solution:
    def solve(self , str ):
        # write code here
        # python字符换不能直接更改，所以转成数组
        s = list(str)
        lt, rt = 0, len(str)-1
        while lt < rt:
            s[lt], s[rt] = s[rt], s[lt]
            lt += 1
            rt -= 1
        return "".join(s)