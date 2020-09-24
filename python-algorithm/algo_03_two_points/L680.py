#--coding:utf-8--
'''
@Time   : 2020/9/24
@Author : Heng Li
@Email  : liheng_lulia@163.com
'''

# 这道题易出错
class Solution:
    def validPalindrome(self, s: str) -> bool:
        lt, rt = 0, len(s)-1
        while lt<rt:
            if s[lt] != s[rt]:
                return self.IsPalindrome(s, lt+1, rt) or self.IsPalindrome(s, lt, rt-1)
            lt += 1
            rt -= 1
        return True

    def IsPalindrome(self, s, lt, rt):
        i,j = lt, rt
        while i<j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
