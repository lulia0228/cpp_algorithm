# -*- coding: utf-8 -*-
# @Time    : 2020/10/3 13:42
# @Author  : No Name

# 这道题不太好想到解题方法

# 记录一个字符上次出现的位置，如果两个字符串中的字符上次出现的位置一样，那么就属于同构。
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        preIndexOfS = [-1 for i in range(128)]
        preIndexOfT = [-1 for i in range(128)]
        for i in range(len(s)) :
            if (preIndexOfS[ord(s[i])] != preIndexOfT[ord(t[i])]) :
                return False
            preIndexOfS[ord(s[i])] = i
            preIndexOfT[ord(t[i])] = i
        return True

# 上面更快
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        preIndexOfS, preIndexOfT = {}, {}
        for i in range(len(s)) :
            if s[i] in preIndexOfS and t[i] not in preIndexOfT :
                return False
            if s[i] not in preIndexOfS and t[i] in preIndexOfT :
                return False
            if s[i] in preIndexOfS and t[i] in preIndexOfT and preIndexOfS[s[i]] != preIndexOfT[t[i]] :
                return False
            preIndexOfS[s[i]] = i
            preIndexOfT[t[i]] = i
        return True