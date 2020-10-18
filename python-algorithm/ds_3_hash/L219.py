# -*- coding: utf-8 -*-


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                if i-d[nums[i]] <= k:
                    return True
            # 每个值保存最大的索引即可，无序记录全部索引
            d[nums[i]] = i
        return False
