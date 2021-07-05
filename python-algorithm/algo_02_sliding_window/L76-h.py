#--coding:utf-8--

# 设计了cnt变量表示s的子串中出现t串的字符的个数
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        r_d = collections.defaultdict(int)
        for c in t:
            r_d[c] += 1
        i, j = 0, 0
        cnt = 0
        start, min_len = 0, len(s) + 1
        while j < len(s):
            if s[j] in r_d:
                r_d[s[j]] -= 1
                if r_d[s[j]] >= 0:
                    cnt += 1
            while cnt == len(t):
                if j - i + 1 < min_len:
                    start = i
                    min_len = j - i + 1
                if s[i] in r_d:
                    r_d[s[i]] += 1
                    if r_d[s[i]] >= 1:
                        cnt -= 1
                i += 1
            j += 1
        # min_len == len(s)+1 说明没找到符合题意的窗口
        return s[start:start + min_len] if min_len != len(s) + 1 else ""


if __name__ == "__main__":
    pass