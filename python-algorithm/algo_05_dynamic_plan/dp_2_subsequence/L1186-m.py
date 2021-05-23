# -*- coding: utf-8 -*-

'''left[i]：为从左到右以i结尾的子数组最大和
right[i]：为从右到左以i结尾的子数组最大和
最后的结果：
不删除：max(left)
删除：left[i - 1] + right[i + 1]的最大值'''

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        left = [float('-inf')] * n
        right = [float('-inf')] * n
        left[0] = arr[0]
        right[-1] = arr[-1]
        for i in range(1, n):
            left[i] = max(left[i - 1] + arr[i], arr[i])
        for i in range(n - 2, -1, -1):
            right[i] = max(right[i + 1] + arr[i], arr[i])
        res = max(left)
        for i in range(1, n - 1):
            res = max(res, left[i - 1] + right[i + 1])
        return res

# 另一种dp思路
'''dp[i][0]：不删除元素，以i结尾的连续子数组最大和
dp[i][1]：删除其中一个得到的最大值，有两种情况（1，删除i 2. 不删除i）'''

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n=len(arr)
        ans=float('-inf')
        dp=[[float('-inf')]*2 for _ in range(n+1)]
        for i in range(n):
            dp[i+1][0]=max(dp[i][0]+arr[i],arr[i])
            dp[i+1][1]=max(dp[i][1]+arr[i],dp[i][0])
            ans=max(ans,dp[i+1][0],dp[i+1][1])
        return ans
