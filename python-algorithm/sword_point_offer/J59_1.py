#--coding:utf-8--



# 双端队列

# 1.窗口每向前滑动一次，如果当前队首元素等于num[i-1]将其删除
# 2.保持队列不是单调递增；把队列中的所有小于新加的元素nums[j]的元素全部从队尾删除

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque = collections.deque()
        res = []
        n = len(nums)
        for i, j in zip(range(1 - k, n + 1 - k), range(n)):
            if i > 0 and deque[0] == nums[i - 1]:
                deque.popleft() # 删除 deque 中对应的 nums[i-1]
            while deque and deque[-1] < nums[j]:
                deque.pop() # 保持 deque 递减
            deque.append(nums[j])
            if i >= 0:
                res.append(deque[0]) # 记录窗口最大值
        return res
