# -*- coding: utf-8 -*-
# @Time    : 2020/10/2 8:09
# @Author  : Heng Li
# @File    : L71-m.py
# @Software: PyCharm

# 思路就是把所有'/'之间的目录压入栈，如果是'.' '..' 特殊处理
class Solution:
    def simplifyPath(self, path: str) -> str:
        dir_ls = [p for p in path.split('/') if p != '']
        stk = []
        res = ""
        for i in range(len(dir_ls)):
            if dir_ls[i] == '.':
                continue
            elif dir_ls[i] == '..' :
                if stk != []:
                    stk.pop(-1)
            else:
                stk.append(dir_ls[i])
        if stk == []:
            return "/"
        else:
            # 因为用list模拟stack所以不使用Python的join()
            while stk:
                res = '/'+ stk.pop(-1) + res
            return res