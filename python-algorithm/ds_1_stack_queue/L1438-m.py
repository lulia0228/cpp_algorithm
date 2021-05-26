# -*- coding: utf-8 -*-

# 方法1 滑动窗口+有序集合（含有重复元素的）
# 枚举每个位置作为滑动窗口右端点,将窗口内的元素
# 用特殊的数据结构存下来，能获取到窗口内的最大最小值，并更新窗口
from sortedcontainers import SortedList
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        s = SortedList()
        n = len(nums)
        left = right = ret = 0
        while right < n:
            s.add(nums[right])
            while s[-1] - s[0] > limit:
                s.remove(nums[left])
                left += 1
            ret = max(ret, right - left + 1)
            right += 1
        return ret


# 方法2 滑动窗口+双端队列 时间复杂度O(n)
# 维护2个双端队列，队首分别为当前滑动窗口内的最大和最小值，根据条件更新左侧端点
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        queMax, queMin = deque(), deque()
        left = right = ret = 0
        while right < n:
            while queMax and queMax[-1] < nums[right]:
                queMax.pop()
            while queMin and queMin[-1] > nums[right]:
                queMin.pop()
            queMax.append(nums[right])
            queMin.append(nums[right])
            while queMax and queMin and queMax[0] - queMin[0] > limit:
                if nums[left] == queMin[0]:
                    queMin.popleft()
                if nums[left] == queMax[0]:
                    queMax.popleft()
                left += 1
            ret = max(ret, right - left + 1)
            right += 1
        return ret