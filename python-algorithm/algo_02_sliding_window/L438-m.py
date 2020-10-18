# -*- coding: utf-8 -*-


# 相当于是567题的结果集合
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # record用于记录窗口中可用的p中的字符个数，有点绕
        record = {}
        for c in p:
            if c not in record:
                record[c] = 1
            else:
                record[c] += 1
        lt, rt = 0, 0
        res = []
        cnt = 0 # 标记窗口中出现s1中的字符的个数
        while rt < len(s):
            if s[rt] in p:
                record[s[rt]] -= 1
                if record[s[rt]] >= 0:
                    cnt += 1
            # 收缩窗口左边界
            while rt-lt+1 == len(p):
                if cnt == len(p):
                    res.append(lt)
                if s[lt] in p:
                    record[s[lt]] += 1
                    if record[s[lt]] >= 1:
                        cnt -= 1
                lt += 1
            rt += 1
        return res