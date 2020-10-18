# -*- coding: utf-8 -*-


# 注意和题目557 不一样
# 题目要求不得占用额外空间
class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        i = 0
        while i<len(s):
            word = ""
            while i < len(s) and s[i] != ' ':
                word += s[i]
                i += 1
            if word != "":
                if res == "":
                    res = word
                else:
                    res = word + ' ' + res
            else:
                i += 1

        return res

# 占用额外空间
class Solution:
    def reverseWords(self, s: str) -> str:
        s_l = s.split(' ')
        s_l = [item for item in s_l if item not in ['']]
        return ' '.join(s_l[::-1])