# -*- coding: utf-8 -*-


# 超时
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        d = {}
        for i in range(len(nums)):
            for tmp in range(nums[i]-t, nums[i]+t+1):
                if tmp in d:
                    if i-d[tmp] <= k:
                        return True
            # 每个值保存最大的索引即可
            d[nums[i]] = [i]
        return False


# 解法不好想到
# 把不同差值的元素放入不同的桶
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        bucket = {}
        for i in range(len(nums)):
            nth = nums[i] // (t + 1)
            if nth in bucket:
                return True
            if nth - 1 in bucket and abs(nums[i] - bucket[nth - 1]) <= t:
                return True
            if nth + 1 in bucket and abs(nums[i] - bucket[nth + 1]) <= t:
                return True
            # 每个桶只存放最新的元素，即最大的索引
            bucket[nth] = nums[i]
            if i >= k:
                bucket.pop(nums[i - k] // (t + 1))
        return False