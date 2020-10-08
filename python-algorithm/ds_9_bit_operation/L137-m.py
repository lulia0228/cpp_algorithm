# -*- coding: utf-8 -*-
# @Time    : 2020/10/7 12:56
# @Author  : No Name

# 1 使用哈希标记次数



# 2 位操作，太难想到了
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seenOnce = 0
        seenTwice = 0
        for num in  nums:
            seenOnce = ~seenTwice & (seenOnce ^ num)
            seenTwice = ~seenOnce & (seenTwice ^ num)
        return seenOnce;