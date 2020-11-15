# -*- coding: utf-8 -*-

# 和 leetcode154一样

class Solution:
    def minArray(self, numbers: List[int]) -> int:
        lt, rt = 0, len(numbers) - 1
        if numbers[0] < numbers[-1]:
            return numbers[0]
        elif numbers[0] > numbers[-1]:
            while lt < rt:
                mid = lt + (rt - lt) // 2
                # if numbers[mid] <= numbers[-1]:
                if numbers[mid] <= numbers[rt]:
                    rt = mid
                else:
                    lt = mid + 1
        else:
            while rt > 0 and numbers[rt] == numbers[-1]:
                rt -= 1
            while lt < rt:
                mid = lt + (rt - lt) // 2
                if numbers[mid] <= numbers[rt]:
                    rt = mid
                else:
                    lt = mid + 1
        return numbers[lt]


