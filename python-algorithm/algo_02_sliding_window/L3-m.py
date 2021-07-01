#--coding:utf-8--


# 滑动窗口  模板化
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r_d = {}
        i, j = 0, 0
        ans = 0
        while j < len(s):
            if s[j] not in r_d:
                r_d[s[j]] = 1
            else:
                r_d[s[j]] += 1
            while r_d[s[j]] > 1:
                if s[i] in r_d:
                    r_d[s[i]] -= 1
                i += 1
            ans = max(ans, j - i + 1)
            j += 1
        return ans


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
