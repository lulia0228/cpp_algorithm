#
#
# @param S string字符串
# @param T string字符串
# @return string字符串
#


import collections
class Solution:
    def minWindow(self, S, T):
        # write code here
        if len(S) < len(T): return ""
        r_d = collections.defaultdict(int)
        for c in T:
            r_d[c] += 1
        i, j = 0, 0
        start, length = 0, len(S) + 1
        cnt = 0
        while j < len(S):
            if S[j] in r_d:
                r_d[S[j]] -= 1
                if r_d[S[j]] >= 0:
                    cnt += 1
            while cnt >= len(T):
                # 块内部顺序很重要
                # length = min(length, j-i+1)
                if j - i + 1 < length:
                    length = j - i + 1
                    start = i

                if S[i] in r_d:
                    r_d[S[i]] += 1
                    if r_d[S[i]] >= 1:
                        cnt -= 1
                i += 1
            j += 1

        return S[start:start + length] if length != len(S) + 1 else ""


