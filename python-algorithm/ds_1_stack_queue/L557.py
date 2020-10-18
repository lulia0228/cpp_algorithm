# -*- coding: utf-8 -*-


class Solution:
    def reverseWords(self, s: str) -> str:
        s_l = s.split(' ')
        s_l = [item[::-1] for item in s_l]
        return ' '.join(s_l)

# 反转一个单词可以两端指针交换，也可以使用栈结构