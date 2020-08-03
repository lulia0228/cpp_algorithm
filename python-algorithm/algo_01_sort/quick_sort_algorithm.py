# -*- coding: utf-8 -*-
# @Time    : 2020/8/3 21:12
# @Author  : Heng Li
# @File    : quick_sort_algorithm.py
# @Software: PyCharm

# 5 快速排序
# 时间复杂度 O(nlogn) 空间复杂度  O(logn)-O(n)   从小到大

'''def quick_sort(li, start, end):
    # 分治 一分为二
    # start=end ,证明要处理的数据只有一个
    # start>end ,证明右边没有数据
    if start >= end:
        return
    # 定义两个游标，分别指向0和末尾位置
    left = start
    right = end
    # 把0位置的数据，认为是中间值
    mid = li[left]
    print('mid',mid)
    while left < right:
        # 让右边游标往左移动，目的是找到小于mid的值，放到left游标位置
        while left < right and li[right] >= mid:
            right -= 1
        print(right)
        li[left] = li[right]
        # 让左边游标往右移动，目的是找到大于mid的值，放到right游标位置
        while left < right and li[left] < mid:
            left += 1
        print(left)
        li[right] = li[left]
    # while结束后，把mid放到中间位置，left=right
    li[left] = mid
    print(li)
    # 递归处理左边的数据
    quick_sort(li, start, left-1)
    # 递归处理右边的数据
    quick_sort(li, left+1, end)


# l = [56,26,44,17,71,31,93,55]
# l = [56,26,44,17,12,28,42,71,31,93,55,58,70,89]
l = [56,26,44,17,12,28,42,71,31,85,55,58,70,89]
quick_sort(l,0,len(l)-1)'''




# 6 归并排序
# 时间复杂度 O(nlogn)  空间复杂度  O(N)
'''x = [int(i) for i in input().split(',')]

def gbsort(x):
    length = len(x)
    if length <= 1:
        return x
    mid = length // 2

    left = gbsort(x[:mid])
    right = gbsort(x[mid:])

    left_point, right_pointer = 0, 0
    result = []

    while left_point < len(left) and right_pointer < len(right):
        if left[left_point] <= right[right_pointer]:
            result.append(left[left_point])
            left_point += 1
        else:
            result.append(right_pointer)
            right_pointer += 1

    result += left[left_point:]
    result +=right[right_pointer]

    return result

print(gbsort(x))'''

'''
def merge(a, b):
    print(a,b)
    c = []
    h = j = 0
    while j < len(a) and h < len(b):
        if a[j] < b[h]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1

    if j == len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)
    return c

def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    middle = len(lists)//2
    # print(middle,lists[:middle])
    left = merge_sort(lists[:middle])
    # print('aaa')
    # print('-----',lists[middle:])
    right = merge_sort(lists[middle:])
    return merge(left, right)

if __name__ == '__main__':
    a = [4, 7, 8, 3, 5, 9, 1]
    print(merge_sort(a))
'''