#--coding:utf-8--


# 前缀和，如果遇到的是0 减1 相当于是把0全部替换成-1
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        r_d = {0:-1}
        t_sum = 0
        ans = 0
        for i, val in enumerate(nums):
            t_sum += (1 if val==1 else -1)
            if t_sum not in r_d:
                r_d[t_sum] = i
            else:
                ans = max(ans, i-r_d[t_sum])
        return ans

