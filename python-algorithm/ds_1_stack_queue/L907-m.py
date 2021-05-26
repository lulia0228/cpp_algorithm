#--coding:utf-8--

# class Solution:
#     def sumSubarrayMins(self, arr: List[int]) -> int:
#         sum_ = 0
#         sz = len(arr)
#         for j in range(sz):
#             for i in range(sz-j):
#                 sum_ += min(arr[i:i+j+1])
#         return sum_

# 同84柱状图中的最大矩形

class Solution:
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ans = 0
        A = [float('-inf')] + A + [float('-inf')]
        stack = []
        for i, a in enumerate(A):
            while stack and A[stack[-1]] > a:
                cur = stack.pop()
                # 找到cur两侧第一个≤它的索引
                # cur左侧[stack[-1]+1,cur) cur右侧（cur,i-1]这2个范围内的数字都大于cur对应的数字
                ans += A[cur] * (i-cur) * (cur-stack[-1])
            stack.append(i)
        return ans % (10**9 + 7)
