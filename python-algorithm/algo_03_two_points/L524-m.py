#--coding:utf-8--
'''
@Time   : 2020/9/24
@Author : Heng Li
@Email  : liheng_lulia@163.com
'''
# 和392一样

class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        max_len = 0
        res = []
        for tmp_str in d:
            if self.IsSubstr(s, tmp_str):
                if len(tmp_str) > max_len:
                    res = [tmp_str]
                    max_len = len(tmp_str)
                elif len(tmp_str) == max_len:
                    res.append(tmp_str)
        if res:
            res.sort()
            return res[0]
        else:
            return ""

    def IsSubstr(self, s, t):
        s_i, t_i = 0, 0
        while s_i < len(s) and t_i < len(t):
            if s[s_i] == t[t_i]:
                s_i += 1
                t_i += 1
            else:
                s_i += 1
        return False if t_i != len(t) else True