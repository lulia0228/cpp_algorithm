# -*- coding: utf-8 -*-
# @Time    : 2020/10/6 13:36
# @Author  : No Name

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = [digits[i] for i in range(len(digits))]
        # res = digits
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            tmp = digits[i] + carry
            res[i] = tmp%10
            carry = tmp//10
            # 剪枝，提前终止
            if carry == 0:
                return res
        if carry == 1:
            res.insert(0,1)
        return res