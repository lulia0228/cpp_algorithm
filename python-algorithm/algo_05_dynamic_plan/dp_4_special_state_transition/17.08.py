#--coding:utf-8--
# 这道题，要求2个维度都是单调递增
# 按其中一个维度排序，转化成求另一个维度上的最长上升子序列问题（leetcode300）
# leetcode300原题使用了动态规划；此外，还有一种效率更高的解法二分法。

# 这道题要注意的细节在于：2个维度严格单调，也就是说比如相同身高、不同体重的人 只能选择一个出来叠罗汉；
# 所以在采用第一维度排序的时候，还应保证一点，那就是第一维度相同值的时候、第二维度应该采用降序，避免相同的身高被多次选。

# class Solution:
#     def bestSeqAtIndex(self, height: List[int], weight: List[int]) -> int:
#         features = [(h,w) for h,w in zip(height, weight)]
#         features = sorted(features, key=lambda x:(x[0], -x[1]))
#         # dp[i]表示以features[i]作为结尾的最长递增子序列长度
#         dp = [1]*(len(features))
#         max_len = 1
#         for i in range(1, len(features)):
#             for j in range(i):
#                 if features[i][1]>features[j][1]:
#                     dp[i] = max(dp[j]+1, dp[i])
#             max_len = max(max_len, dp[i])
#         return max_len


class Solution:
    def bestSeqAtIndex(self, height: List[int], weight: List[int]) -> int:
        features = [(h, w) for h, w in zip(height, weight)]
        features = sorted(features, key=lambda x: (x[0], -x[1]))
        '''
        (1)新建数组，record[i]最终表示的是长度为i+1的递增子序列中尾数最小的值；因此record是递增的
        (2)在遍历时通过二分法确定元素应该被放到record中的具体位置，因此时间复杂度是N*logN
        '''
        maxL = 0
        record = [0] * (len(features))
        for fea in features:
            lt, rt = 0, maxL
            while lt < rt:
                mid = lt + (rt - lt) // 2
                if record[mid][1] < fea[1]:
                    lt = mid + 1
                else:
                    rt = mid
            record[lt] = fea
            if lt == maxL:
                maxL += 1
        return maxL