# -*- coding: utf-8 -*-

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        sz = len(s)
        for inteval in range(1, sz//2+1):
            # 必须要有，长度必须被间隔整除才可以，否则例如aabaaba下面会通过判定
            if sz%inteval != 0:
                continue
            # all 里面做成迭代器速度更快
            if all( (s[i]==s[i+inteval] for i in range(sz-inteval)) ):
                return True
        return False



