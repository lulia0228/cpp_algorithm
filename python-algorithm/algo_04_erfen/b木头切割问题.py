# -*- coding: utf-8 -*-

'''
题目描述
给定长度为n的数组，每个元素代表一个木头的长度，木头可以任意截断，从这堆木头中截出至少k个相同长度为m的木块。已知k，求max(m)。
输入两行，第一行n, k，第二行为数组序列。输出最大值。
ps:数据保证有解，即结果至少是1。
'''

# 暴力法：枚举每个可能的最大长度
def findMax(n, k, arr):
    maxK = max(arr)
    res = 1
    m = 1
    while m <= maxK:
        cnt = 0
        for i in range(n):
            cnt += arr[i]//m
        if cnt >= k:
            res = max(res, m)
    return res

# 优化：二分法
# 上面在对长度进行[1, maxK]的过程中可以采用二分法寻找最大的m

def findMax(n, k, arr):
    def get(arr, m):
        cnt = 0
        for i in range(n):
            cnt += arr[i]//m
        return cnt

    lt, rt = 1, max(arr)
    while lt < rt:
        mid = lt + (rt-lt + 1)//2
        if get(arr, mid) >= k :
            lt = mid
        else:
            rt = mid-1
    return rt