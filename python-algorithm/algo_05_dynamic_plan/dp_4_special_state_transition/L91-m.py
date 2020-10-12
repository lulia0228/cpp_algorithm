#--coding:utf-8--
'''
@Time   : 2020/10/12
@Author : No Name
'''

class Solution:
    def numDecodings(self, s: str) -> int:
        # 先判断能否解码: (1)0开头的不行 （2）0字符前面的数字大于2 （3）连续出现0个数大于1
        for i in range(len(s)):
            if s[i] == "0":
                if i==0 or int(s[i-1])>2:
                    return 0
                cnt = 0
                while i<len(s) and s[i]=="0":
                    cnt += 1
                    i += 1
                if cnt > 1:
                    return 0

        sz = len(s)
        dp = [0]*(sz+1)
        dp[0] = 1 # 空也是一种解码方法
        dp[1] = 1
        for i in range(2, sz+1):
            if s[i-1] == '0':
                dp[i] = dp[i-2]
            else:
                tmp = int(s[i-2:i])
                if tmp > 10 and tmp <= 26:
                    dp[i] = dp[i-1]+dp[i-2]
                else:
                    dp[i] = dp[i-1]
        return dp[sz]

