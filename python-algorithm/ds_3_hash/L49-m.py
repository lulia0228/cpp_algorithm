# -*- coding: utf-8 -*-
# @Time    : 2020/10/1 19:58
# @Author  : Heng Li
# @File    : L49-m.py
# @Software: PyCharm

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        res = []
        for s in strs:
            # 注意python对string使用sorted会生成字符列表
            ref = ''.join(sorted(s))
            if ref not in d:
                d[ref] = [s]
            else:
                d[ref].append(s)
        for k,v in d.items():
            res.append(v)
        return res

