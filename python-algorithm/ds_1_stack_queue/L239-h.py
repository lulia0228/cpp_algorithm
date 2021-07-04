#--coding:utf-8--

# 单调栈
import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        sz = len(nums)
        q = collections.deque()
        # 注意下面的区间设置；容易多1或者少1
        for st, et in zip(range(-k+1, sz-k+1), range(sz)):
            if st>0 and nums[st-1] == q[0]:
                q.popleft()
            while q and q[-1]<nums[et]:
                q.pop()
            q.append(nums[et])
            if st>=0 :
                res.append(q[0])
        return res