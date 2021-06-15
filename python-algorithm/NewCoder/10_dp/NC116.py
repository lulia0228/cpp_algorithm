#--coding:utf-8--

class Solution:
    def solve(self , nums ):
        # write code here
        sz = len(nums)
        dp = [0]*(sz+1)
        dp[0] = 1
        for i in range(1, sz+1):
            # 判断不能解码的情况；直接程序返回
            if nums[i-1]=="0" and (i==1 or int(nums[i-2])>2 or int(nums[i-2])<1):
                return 0
            if nums[i-1] == "0":
                dp[i] = dp[i-2]
            else:
                if i>1 and 10<int(nums[i-2:i])<=26:
                    dp[i] = dp[i-1]+dp[i-2]
                else:
                    dp[i] = dp[i-1]
        return dp[sz]

# res = Solution().solve("10")
res = Solution().solve("72416145196211821232022471311148103136128331523141061051992231223")
print(res)

# 11520000