# -*- coding: utf-8 -*-

# 归并排序
# 时间复杂度 O(nlogn)  空间复杂度  O(N)

def merge(a, b):
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

def gb_sort(lists):
    if len(lists) <= 1:
        return lists
    mid = len(lists)//2
    left = gb_sort(lists[:mid])
    right = gb_sort(lists[mid:])
    return merge(left, right)



if __name__ == '__main__':
    a = [4, 7, 8, 3, 5, 9, 1]
    print(gb_sort(a))
