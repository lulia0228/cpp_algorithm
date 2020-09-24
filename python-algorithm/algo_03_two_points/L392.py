#--coding:utf-8--
'''
@Time   : 2020/9/24
@Author : Heng Li
@Email  : liheng_lulia@163.com
'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_i, t_i = 0, 0
        while s_i < len(s) and t_i < len(t):
            if t[t_i] == s[s_i]:
                s_i += 1
                t_i += 1
            else:
                t_i += 1
        return False if s_i != len(s) else True