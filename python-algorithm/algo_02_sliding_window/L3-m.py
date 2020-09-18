#--coding:utf-8--
'''
@Time   : 2020/9/18
@Author : Heng Li
@Email  : liheng_lulia@163.com
'''

# 滑动窗口  模板化
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        record = {}
        # 用python需要提前初始化字典
        for char in s:
            record[char] = 0
        lt,rt = 0,0
        res = 1
        while rt < len(s):
            c = s[rt]
            # 进行窗口内数据的一系列更新
            record[c] += 1
            # 判断左侧窗口是否要收缩
            while record[c] > 1:
                d = s[lt]
                lt += 1
                # 进行窗口内数据的一系列更新
                record[d] -= 1
            res = max(res, rt-lt+1)
            rt += 1
        return res


# 双指针
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        res = 1
        start = 0
        for j in range(1,len(s),1):
            k = start
            while k < j :
                if s[k] == s[j]:
                    start = k+1
                    break
                k += 1
            res = max(res, j-start+1)
        return res
