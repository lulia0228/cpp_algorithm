# -*- coding: utf-8 -*-
# @Time    : 2020/10/7 18:49
# @Author  : No Name

# 没太搞懂这题
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x: (-x[0], x[1]))
        output = []
        for p in people:
            output.insert(p[1], p)
        return output

