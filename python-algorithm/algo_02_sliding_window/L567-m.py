# -*- coding: utf-8 -*-


# 滑动窗口

# 1 收缩窗口 判断条件：排序后是否相等，速度比较慢
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lt, rt = 0, 0
        goal = self.sort_string(s1)
        while rt < len(s2):
            while rt-lt+1 == len(s1):
                if self.sort_string(s2[lt:rt+1]) == goal:
                    return True
                lt += 1
            rt += 1
        return False

    def sort_string(self, s):
        return "".join((lambda x: (x.sort(), x)[1])(list(s)))


# 2 收缩窗口的判断条件，巧妙的设计了一个变量cnt（76题也可以这么做），来判断子串是不是s1的排列
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # record用于记录窗口中可用的s1中的字符个数，有点绕
        record = {}
        for c in s1:
            if c not in record:
                record[c] = 1
            else:
                record[c] += 1
        lt, rt = 0, 0
        cnt = 0 # 标记窗口中出现s1中的字符的个数
        while rt < len(s2):
            if s2[rt] in s1:
                record[s2[rt]] -= 1
                if record[s2[rt]] >= 0:
                    cnt += 1
            # 收缩窗口左边界
            while rt-lt+1 == len(s1):
                if cnt == len(s1):
                    return True
                if s2[lt] in s1:
                    record[s2[lt]] += 1
                    if record[s2[lt]] >= 1:
                        cnt -= 1
                lt += 1
            rt += 1
        return False

