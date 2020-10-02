# -*- coding: utf-8 -*-
# @Time    : 2020/10/2 9:40
# @Author  : Heng Li
# @File    : L394-m.py
# @Software: PyCharm

class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        res = ""
        for c in s:
            if c != ']':
                stk.append(c)
            else:
                tmp_str = ""
                while stk[-1] != '[':
                    tmp_str = stk[-1]+tmp_str
                    stk.pop(-1)
                stk.pop(-1)
                # 容易考虑不到就是重复次数不是1位的整数
                cnt_str = ""
                # 必须判断为空，否则访问越界报错
                while stk and stk[-1].isdigit():
                    cnt_str = stk.pop(-1) + cnt_str
                cnt = int(cnt_str)
                stk.append(tmp_str*cnt)
        # 这里用python list模拟c++中的stack，最好不要使用Python的字符串join()
        while stk:
            res = stk.pop(-1) + res
        return res