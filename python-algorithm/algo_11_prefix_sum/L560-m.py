#--coding:utf-8--
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        r_d = collections.defaultdict(int)
        r_d[0] = 1
        t_sum = 0
        ans = 0
        for i in range(len(nums)):
            t_sum += nums[i]
            if t_sum-k in r_d:
                ans += r_d[t_sum-k]
            r_d[t_sum] += 1
        return ans
