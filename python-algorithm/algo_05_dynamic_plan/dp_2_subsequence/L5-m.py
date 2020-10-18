#--coding:utf-8--


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == "":
            return ""
        start, max_len = 0, 1
        sz = len(s)
        dp = [[0 for i in range(sz)] for i in range(sz)]
        for i in range(sz):
            j = i
            while j >= 0:
                if s[j] == s[i] and (i - j < 2 or dp[j + 1][i - 1]):
                    dp[j][i] = 1
                    # 这里可优化，没必要对当前i为结尾的所有字符串计算长度，只需标记最小的起点，在循环外面计算一次
                    tmp_len = i - j + 1
                    if tmp_len > max_len:
                        max_len = tmp_len
                        start = j
                j -= 1
        return s[start:start + max_len]


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == "":
            return ""
        start, max_len = 0, 1
        sz = len(s)
        dp = [[0 for i in range(sz)] for i in range(sz)]
        for i in range(sz):
            j = i
            cur_min_start = 0
            while j >= 0:
                if s[j] == s[i] and (i - j < 2 or dp[j + 1][i - 1]):
                    dp[j][i] = 1
                    cur_min_start = j
                j -= 1
            tmp_len = i - cur_min_start + 1
            if tmp_len > max_len:
                max_len = tmp_len
                start = cur_min_start
        return s[start:start + max_len]


# 中心扩展比动态规划快太多
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == "":
            return ""
        start, max_len = 0, 1
        sz = len(s)
        for i in range(sz):
            min_cur_start = 0
            # 当前字母是奇数长度回文子串的中点
            lt, rt = i - 1, i + 1
            while lt >= 0 and rt < sz and s[lt] == s[rt]:
                lt -= 1
                rt += 1
            if rt-lt-1 > max_len:
                start = lt+1
                max_len = rt-lt-1
            # 当前字母是偶数长度回文子串的中点
            lt, rt = i - 1, i
            while lt >= 0 and rt < sz and s[lt] == s[rt]:
                lt -= 1
                rt += 1
            if rt-lt-1 > max_len:
                start = lt+1
                max_len = rt-lt-1
        return s[start: start+max_len]

res = "cbbd"
print(Solution().longestPalindrome(res))


