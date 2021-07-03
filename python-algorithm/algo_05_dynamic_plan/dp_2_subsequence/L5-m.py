#--coding:utf-8--

# 动态规划
class Solution:
    def longestPalindrome(self, s: str) -> str:
        sz = len(s)
        start = 0
        max_len = 1
        dp = [[0]*sz for _ in range(sz)]
        for i in range(sz):
            dp[i][i] = 1
        for i in range(sz):
            j = i-1
            while j>=0:
                if s[j] == s[i] and(i-j<2 or dp[j+1][i-1]):
                    dp[j][i] = 1
                    if i-j+1>max_len:
                        start = j
                        # 可以做一点优化；下面一句放在while外部
                        max_len = i-j+1
                j -= 1
        return s[start:start+max_len]



# 中心扩展
class Solution1:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        max_len = 1
        for i in range(len(s)):
            lt, rt = i - 1, i + 1
            # i为回文串中点
            while lt >= 0 and rt < len(s):
                if s[lt] == s[rt]:
                    lt -= 1
                    rt += 1
                else:
                    break

            if rt - lt - 1 > max_len:
                start = lt + 1
                max_len = rt - lt - 1

            # i不为回文串中点
            lt, rt = i - 1, i
            while lt >= 0 and rt < len(s):
                if s[lt] == s[rt]:
                    lt -= 1
                    rt += 1
                else:
                    break

            if rt - lt - 1 > max_len:
                start = lt + 1
                max_len = rt - lt - 1
        return s[start:start + max_len]


res = "cbbd"
print(Solution1().longestPalindrome(res))


