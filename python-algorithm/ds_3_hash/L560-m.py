# -*- coding: utf-8 -*-


# 560 和为k的连续子数组

# 乍一看，想用滑窗，用哈希记录下每个位置处的累加和即可
# 哈希的value也可以不用list存实际索引，只需要存计数也可以
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {0:[-1]}
        tmp_sum = 0
        res = 0
        for i in range(len(nums)):
            tmp_sum += nums[i]
            tmp = tmp_sum-k
            if tmp in d:
                res += len(d[tmp])
            if tmp_sum not in d:
                d[tmp_sum] = [i]
            else:
                d[tmp_sum].append(i)
        return res