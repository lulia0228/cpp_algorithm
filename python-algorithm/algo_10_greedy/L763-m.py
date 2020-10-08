# -*- coding: utf-8 -*-
# @Time    : 2020/10/7 19:14
# @Author  : No Name

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {c: i for i, c in enumerate(S)}
        end = start = 0
        ans = []
        for i, c in enumerate(S):
            # 标记局部最靠后的索引位置
            end = max(end, last[c])
            if i == end:
                ans.append(i - start + 1)
                start = i + 1
        return ans

# 另一种写法是记录下每个字母的起始结束区间，形成一组区间，然后转化成56题的合并区间的做法
