# -*- coding: utf-8 -*-

# 类似环链表检测2
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        slow = nums[slow]
        fast = nums[nums[fast]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        pre1, pre2 = 0, slow
        while pre1 != pre2:
            pre1 = nums[pre1]
            pre2 = nums[pre2]

        return pre1


