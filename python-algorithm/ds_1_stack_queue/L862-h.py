#--coding:utf-8--

# 前缀和+双端单调队列
class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        prefix = [0]
        for n in A:
            prefix.append(prefix[-1]+n)
        q = collections.deque()
        ans = len(A)+1
        for idx, val in enumerate(prefix):
            # 单调递增前缀和队列（题目中K>0）
            while q and prefix[q[-1]] > val:
                q.pop()
            while q and prefix[q[0]]+K<=val:
                ans = min(ans, idx-q.popleft())
            q.append(idx)
        return ans if ans < len(A)+1 else -1