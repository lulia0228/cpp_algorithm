# -*- coding: utf-8 -*-


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        res = ""
        min_len = inf
        for word in strs:
            min_len = min(min_len, len(word))
        for i in range(min_len):
            ref = strs[0][i]
            flag = 1
            for j in range(len(strs)):
                if strs[j][i] != ref :
                    flag = 0 # 说明遍历过程中找到了不同的字符
                    break # 注意break只能终止当前层的循环，无法终止外部层的循环
            if flag:
                res += ref
            else:
                break
        return res

# 巧妙借助python内部的字符串排序
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs: return ""
        s1 = min(strs)
        s2 = max(strs)
        for i,x in enumerate(s1):
            if x != s2[i]:
                return s2[:i]
        return s1