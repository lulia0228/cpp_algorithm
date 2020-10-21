#--coding:utf-8--

# 设计了cnt变量表示s的子串中出现t串的字符的个数
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lt, rt = 0, 0
        min_len_start = 0
        min_len = len(s)+1
        record = {}
        for char in t:
            if char not in record:
                record[char] = 1
            else:
                record[char] += 1
        cnt = 0
        while rt < len(s):
            c = s[rt]
            if c in t:
                record[c] -= 1
                if record[c] >= 0:
                    cnt += 1
            while cnt >= len(t):
                if rt-lt+1 < min_len:
                    min_len_start = lt
                    min_len = rt-lt+1
                d = s[lt]
                if d in t:
                    record[d] += 1
                    if record[d] >= 1:
                        cnt -= 1
                lt += 1
            rt += 1
        return  "" if min_len>len(s) else s[min_len_start:min_len_start+min_len]


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lt, rt = 0, 0
        min_len_start = 0
        min_len = len(s)+1
        record = {}
        for char in s:
            if char in t:
                record[char] = 0
        while rt < len(s):
            c = s[rt]
            if c in t:
                record[c] += 1
            while self.contain_t(record, t):
                if rt-lt+1 < min_len:
                    min_len_start = lt
                    min_len = rt-lt+1
                d = s[lt]
                if d in t:
                    record[d] -= 1
                lt += 1
            rt += 1
        return  "" if min_len>len(s) else s[min_len_start:min_len_start+min_len]

    def contain_t(self, record, t):
        t_d = {}
        for c in t:
            if c not in t_d:
                t_d[c] = 1
            else:
                t_d[c] += 1
        for k,v in t_d.items():
            if k not in record or record[k] < v:
                return False
        return True


if __name__ == "__main__":
    pass