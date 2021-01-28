#--coding:utf-8--
class Solution:
    def findSquare(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        # dp1[i][j]表示以matrix[i-1][j-1]作为右下角的块向上的0个数
        # dp2[i][j]表示以matrix[i-1][j-1]作为右下角的块向左的0个数
        dp1 = [[0]*(n+1) for i in range(m+1)]
        dp2 = [[0]*(n+1) for i in range(m+1)]
        max_len = 0
        res = [-1, -1, 0]
        for i in range(1,m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1]==0:
                    dp1[i][j] = dp1[i-1][j]+1
                    dp2[i][j] = dp2[i][j-1]+1
                    bound = min(dp1[i][j], dp2[i][j])
                    for k in range(bound):
                        if dp2[i-k][j]>=k+1 and dp1[i][j-k]>=k+1:
                            if k+1>max_len:
                                max_len = k+1
                                res[0] = i-k-1
                                res[1] = j-k-1
                                res[2] = max_len
                            elif k+1==max_len:
                                if i-k-1<res[0]:
                                    res[0] = i-k-1
                                    res[1] = j-k-1
                                    res[2] = max_len
                                elif i-k-1==res[0]:
                                    if j-k-1<res[1]:
                                        res[0] = i-k-1
                                        res[1] = j-k-1
                                        res[2] = max_len
        return [] if res==[-1,-1,0] else res