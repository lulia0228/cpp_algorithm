#--coding:utf-8--
# 给你一个整型数组 nums ，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

# 排序后取三个最大数乘积和2个最小负数与最大正数的乘积中较大的一个即可

class Solution:
    def maximumProduct(self, A: List[int]) -> int:
        sz = len(A)
        fisrt_big, second_big, third_big = -float("inf"), -float("inf"), -float("inf")
        first_small, second_small = float("inf"), float("inf")
        for i in range(sz):
            if third_big < A[i] <= second_big:
                third_big = A[i]
            elif second_big< A[i]<= fisrt_big:
                third_big = second_big
                second_big = A[i]
            elif A[i] > fisrt_big:
                third_big = second_big
                second_big = fisrt_big
                fisrt_big = A[i]

            if first_small <= A[i] < second_small:
                second_small =  A[i]
            elif A[i] < first_small:
                second_small = first_small
                first_small = A[i]
        # print(fisrt_big, second_big, third_big, first_small, second_small)
        return max(first_small * second_small * fisrt_big, fisrt_big * second_big * third_big)