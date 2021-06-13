# -*- coding: utf-8 -*-
# 数字在升序数组中出现的次数
# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if not data: return 0
        lt, rt = 0, len(data) - 1
        # 找第一次出现的target
        while lt < rt:
            mid = lt + (rt - lt) // 2
            if data[mid] >= k:
                rt = mid
            else:
                lt = mid + 1

        if data[lt] == k:
            idx, cnt = lt, 0
            while idx < len(data) and data[idx] == k:
                cnt += 1
                idx += 1
            return cnt
        else:
            return 0

