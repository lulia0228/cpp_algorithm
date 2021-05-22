#--coding:utf-8--

# 前缀和+堆/二分(值)

class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = matrix[0][0]
        for i in range(1,m):
            dp[i][0] = dp[i-1][0]^matrix[i][0]
        for j in range(1,n):
            dp[0][j] = dp[0][j-1]^matrix[0][j]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j]^dp[i][j-1]^dp[i-1][j-1]^matrix[i][j]
        myheap = []
        for i in range(m):
            for j in range(n):
                if len(myheap)<k:
                    heapq.heappush(myheap, dp[i][j])
                elif dp[i][j]>myheap[0]:
                    heapq.heappop(myheap)
                    heapq.heappush(myheap, dp[i][j])
        return myheap[0]
