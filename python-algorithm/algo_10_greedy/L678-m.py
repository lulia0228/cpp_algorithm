#--coding:utf-8--

# lo、hi表示可能多余的最少、最多左括号
# 1 遇到左括号：lo++, hi++
# 2 遇到星号：lo--, hi++（因为星号有三种情况）
# 3 遇到右括号：lo--, hi--
# lo要保持不小于0。
# 如果hi < 0，说明把星号全变成左括号也不够了
# 如果lo > 0，说明末尾有多余的左括号

# 贪心算法
class Solution(object):
    def checkValidString(self, s):
        lo = hi = 0
        for c in s:
            lo += 1 if c == '(' else -1
            hi += 1 if c != ')' else -1
            if hi < 0:
                return False
            lo = max(lo, 0)
        return lo == 0



class Solution1(object):
    def checkValidString(self, s):
        if not s: return True
        LEFTY, RIGHTY = '(*', ')*'

        n = len(s)
        dp = [[False] * n for _ in s]
        for i in xrange(n):
            if s[i] == '*':
                dp[i][i] = True
            if i < n-1 and s[i] in LEFTY and s[i+1] in RIGHTY:
                dp[i][i+1] = True

        for size in xrange(2, n):
            for i in xrange(n - size):
                if s[i] == '*' and dp[i+1][i+size]:
                    dp[i][i+size] = True
                elif s[i] in LEFTY:
                    for k in xrange(i+1, i+size+1):
                        if (s[k] in RIGHTY and
                                (k == i+1 or dp[i+1][k-1]) and
                                (k == i+size or dp[k+1][i+size])):
                            dp[i][i+size] = True

        return dp[0][-1]
