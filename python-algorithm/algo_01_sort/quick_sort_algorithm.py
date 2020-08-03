# -*- coding: utf-8 -*-
# @Time    : 2020/8/3 21:12
# @Author  : Heng Li
# @File    : quick_sort_algorithm.py
# @Software: PyCharm

# 快速排序
# 时间复杂度 O(nlogn) 空间复杂度  O(logn)-O(n)   从小到大

def quick_sort(li, left, right):
    # 分治 一分为二
    # left=right ,证明要处理的数据只有一个
    # left>right ,证明右边没有数据
    if left >= right:
        return
    # 定义两个游标，分别指向0和末尾
    i = left
    j = right
    # 把0位置的数据，认为是中间值
    mid = li[i]
    while i < j:
        # 让右边游标往左移动，目的是找到小于mid的值，放到i游标位置
        while i < j and li[j] >= mid:
            j -= 1
        li[i] = li[j]
        # 让左边游标往右移动，目的是找到大于mid的值，放到j游标位置
        while i < j and li[i] <= mid:
            i += 1
        li[j] = li[i]
    # while结束后，把mid放到中间位置，i=j
    li[i] = mid
    # 递归处理左边的数据
    quick_sort(li, left, i-1)
    # 递归处理右边的数据
    quick_sort(li, i+1, right)

def quick_sort_2(li, left, right):
    # 分治 一分为二
    # left=right ,证明要处理的数据只有一个
    # left>right ,证明右边没有数据
    if left >= right:
        return
    # 定义两个游标，分别指向0和末尾
    i = left
    j = right
    # 把0位置的数据，认为是中间值
    mid = li[i]
    while i < j:
        # 让右边游标往左移动，目的是找到小于mid的值，放到i游标位置
        while i < j and li[j] >= mid:
            j -= 1
        # 让左边游标往右移动，目的是找到大于mid的值，放到j游标位置
        while i < j and li[i] <= mid:
            i += 1
        li[i],li[j] = li[j],li[i]
    # while结束后，把mid放到中间位置，i=j
    li[left],li[i] = li[i],li[left]
    # 递归处理左边的数据
    quick_sort(li, left, i-1)
    # 递归处理右边的数据
    quick_sort(li, i+1, right)


if __name__ == '__main__':
    # a = [4, 7, 8, 3, 5, 9, 1]
    a = [56, 26, 44, 17, 12, 28, 42, 71, 31, 85, 55, 58, 70, 89]
    quick_sort(a, 0, len(a) - 1)
    # quick_sort_2(a, 0, len(a) - 1)
    print(a)
