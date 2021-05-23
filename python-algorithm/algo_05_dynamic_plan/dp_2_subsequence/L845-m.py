# -*- coding: utf-8 -*-
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        max_len = 0
        idx = 1
        while idx < len(arr)-1:
            nxt = idx+1
            if arr[idx]>arr[idx-1] and arr[idx]>arr[idx+1]:
                cnt = 3
                left = idx-2
                while left>=0 and arr[left]<arr[left+1]:
                    cnt += 1
                    left -= 1
                right = idx+2
                while right<len(arr) and arr[right]<arr[right-1]:
                    cnt += 1
                    right += 1
                max_len = max(max_len, cnt)
                nxt = right # 下标更新到当前山脉的右下脚
            idx = nxt
        return max_len

# DP
# left[i]表示arr[i]向左侧最多可以扩展的元素数目
# right[i]表示arr[i]向右侧最多可以扩展的元素数目
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        sz = len(arr)
        left = [0]*sz
        right = [0]*sz
        for i in range(1, sz):
            left[i] = (left[i-1]+1 if arr[i]>arr[i-1] else 0)
        for j in range(sz-2, -1, -1):
            right[j] = (right[j+1]+1 if arr[j]>arr[j+1] else 0)
        max_len = 0
        for i in range(sz):
            if left[i] and right[i]:
                max_len = max(max_len, right[i]+left[i]+1)
        return max_len