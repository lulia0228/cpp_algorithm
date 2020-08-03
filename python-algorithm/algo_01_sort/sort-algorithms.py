# -*- coding: utf-8 -*-
# @Time    : 2020/8/3 21:11
# @Author  : Heng Li
# @File    : sort-algorithms.py
# @Software: PyCharm


# 1 冒泡排序
def bubbleSort(x):
    n = len(x)
    for i in range(n-1):
        for j in range(0, n-i-1): # 第一轮下来最大的一定在最后位置   最后排序完是从小到大
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]

        # for j in range(0, n-i-1):  # 第一轮下来最小的一定在最后位置  最后排序完是从大到小
        #     if x[j] < x[j + 1]:
        #         x[j], x[j + 1] = x[j + 1], x[j]
    return x


# 2 插入排序：
def insertionSort(x):
    n = len(x)
    for i in range(1,n):
        val = x[i]
        for j in range(i-1,-1,-1):
            if val < x[j]:
                x[j+1] = x[j] # 相当于把val一直往前交换
            else:
                break
        x[j+1] = val
    return x

# 3 选择排序：
def selectionSort(x):
    n = len(x)
    for i in range(1,n):
        minIndex = i
        for j in range(i+1,n):
            if x[j] < x[minIndex]:
                minIndex = j # 在未排序区间找到最小值
        x[i],x[minIndex] = x[minIndex],x[i]
    return x

if __name__ == "__main__":
    test_list = [3,1,5,2,4,8,7]
    print(bubbleSort(test_list))
    print(insertionSort(test_list))
    print(selectionSort(test_list))