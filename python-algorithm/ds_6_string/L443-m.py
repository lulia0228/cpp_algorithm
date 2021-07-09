# -*- coding: utf-8 -*-
# 压缩字符串

class Solution:
    def compress(self, chars: List[str]) -> int:
        i, flag = 0, chars[0]
        cnt = 1
        for j in range(1, len(chars)+1):
            if j==len(chars) or chars[j] != flag:
                chars[i] = flag
                i += 1
                if cnt > 1:
                    t_str = str(cnt)
                    for c in t_str:
                        chars[i] = c
                        i += 1
                if j<len(chars):
                    flag = chars[j]
                    cnt = 1
            else:
                cnt += 1
        return i

