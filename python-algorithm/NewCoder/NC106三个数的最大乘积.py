# -*- coding: utf-8 -*-
class Solution:
    def solve(self, A):
        # write code here
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
        print(fisrt_big, second_big, third_big, first_small, second_small)
        return max(first_small * second_small * fisrt_big, fisrt_big * second_big * third_big)

res = Solution().solve([3,4,1,2])
print(res)