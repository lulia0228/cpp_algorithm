# -*- coding: utf-8 -*-
# @Time    : 2020/10/1 19:47
# @Author  : Heng Li
# @File    : L38.py
# @Software: PyCharm

class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        for i in range(1, n):
            res = self.next_item(res)
        return res

    def next_item(self, s):
        res = ""
        cnt = 0
        flag = s[0]
        i = 0
        while i < len(s):
            # 所有判断索引越界的条件（i<len(s)）应该放在最靠前
            while i < len(s) and s[i] == flag:
                cnt += 1
                i += 1
            res += str(cnt)
            res += flag
            if i < len(s):
                flag = s[i]
                cnt = 0
        return res