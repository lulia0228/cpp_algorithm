#--coding:utf-8--
'''
@Time   : 2020/9/24
@Author : Heng Li
@Email  : liheng_lulia@163.com
'''

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        lt, rt = 0, len(s)-1
        while lt < rt:
            s[lt], s[rt] = s[rt], s[lt]
            lt += 1
            rt -= 1

