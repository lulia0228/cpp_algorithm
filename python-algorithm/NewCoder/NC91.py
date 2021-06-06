#--coding:utf-8--

#
# retrun the longest increasing subsequence
# @param arr int整型一维数组 the array
# @return int整型一维数组
#

import copy

class Solution:
    def LIS(self, arr):
        # write code here
        if len(arr) == 0: return []
        reserve = [[[arr[i]]] for i in range(len(arr))]
        dp = [1] * len(arr)
        for i in range(1, len(arr)):
            for j in range(i):
                if arr[i] > arr[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        seq = reserve[j][0]
                        new_seq = copy.deepcopy(seq)
                        new_seq.append(arr[i])
                        # print(new_seq)
                        reserve[i] = [new_seq]
                    elif dp[j] + 1 == dp[i]:
                        for seq in reserve[j]:
                            new_seq = copy.deepcopy(seq)
                            new_seq.append(arr[i])
                            # print(new_seq)
                            reserve[i].append(new_seq)
                        reserve[i].sort()
                        reserve[i] = [reserve[i][0]]

        for item in reserve:
            print(item)
        max_len = 1
        max_idx = []
        for i in range(len(dp)):
            if dp[i] > max_len:
                max_len = dp[i]
                max_idx = [i]
            elif dp[i] == max_len:
                max_idx.append(i)
        res = []
        for idx in max_idx:
            for ss in reserve[idx]:
                res.append(ss)
        res = sorted(res)
        return res[0]



import copy
class Solution1:
    def LIS(self , arr ):
        # write code here
        if len(arr) == 0: return []
        reserve = [[[arr[i]]] for i in range(len(arr))]
        dp = [1]*len(arr)
        for i in range(1,len(arr)):
            for j in range(i):
                if arr[i] > arr[j]:
                    if dp[j]+1 > dp[i]:
                        dp[i] = dp[j]+1
                        tmp = []
                        for seq in reserve[j]:
                            new_seq = copy.deepcopy(seq)
                            new_seq.append(arr[i])
                            # print(new_seq)
                            tmp.append(new_seq)
                        reserve[i] = tmp
                    elif dp[j]+1 == dp[i]:
                        for seq in reserve[j]:
                            new_seq = copy.deepcopy(seq)
                            new_seq.append(arr[i])
                            # print(new_seq)
                            reserve[i].append(new_seq)
        # for item in reserve:
        #     print(item)
        max_len = 1
        max_idx = []
        for i in range(len(dp)):
            if dp[i] > max_len:
                max_len = dp[i]
                max_idx = [i]
            elif dp[i] == max_len:
                max_idx.append(i)
        res = []
        for idx in max_idx:
            for ss in reserve[idx]:
                res.append(ss)
        res = sorted(res)
        return res[0]

arr = [2,1,5,3,6,4,8,9,7]

res = Solution().LIS(arr)
print(res)