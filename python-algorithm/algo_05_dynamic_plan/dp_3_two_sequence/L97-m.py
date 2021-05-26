#--coding:utf-8--

# f(i,j)表示s1的前i个字符和s2的前j个字符是否可以交叉组成s3的前i+j个元素

# 状态转移方程：
# p = i+j-1
# f(i,j)=（ f(i−1,j) and s1(i−1)=s3(p) ）or （ f(i,j−1) and s2(j−1)=s3(p) ）

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len1=len(s1)
        len2=len(s2)
        len3=len(s3)
        if(len1+len2!=len3):
            return False
        dp=[[False]*(len2+1) for i in range(len1+1)]
        dp[0][0]=True
        for i in range(1,len1+1):
            dp[i][0]=(dp[i-1][0] and s1[i-1]==s3[i-1])
        for i in range(1,len2+1):
            dp[0][i]=(dp[0][i-1] and s2[i-1]==s3[i-1])
        for i in range(1,len1+1):
            for j in range(1,len2+1):
                dp[i][j]=(dp[i][j-1] and s2[j-1]==s3[i+j-1]) or (dp[i-1][j] and s1[i-1]==s3[i+j-1])
        return dp[-1][-1]
