#--coding:utf-8--
'''
@Time   : 2020/10/9
@Author : No Name
'''

# 贪心算法，起始和题目leetcode435删除区间，使剩下的不重叠区间最多  类似
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        cnt = 0
        ref = pairs[0]
        for i in range(1, len(pairs)):
            if pairs[i][0] <= ref[1]:
                cnt += 1
            else:
                ref = pairs[i]
        return len(pairs) - cnt


# 动态规划，和leetcode300最长上升子序列类似做法
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        sz = len(pairs)
        pairs.sort(key=lambda x:x[0])
        # dp[i]表示以pairs[i]作为结尾的最大长度
        dp = [1]*sz
        max_len = 1
        for i in range(1, sz):
            for j in range(i):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[i], dp[j]+1)
            max_len = max(max_len, dp[i])
        return max_len
