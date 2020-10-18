# -*- coding: utf-8 -*-


class Solution:
    def singleNumber(self, nums: int) -> List[int]:
        # difference between two numbers (x and y) which were seen only once
        bitmask = 0
        # 异或，相同为0，不同为1
        for num in nums:
            bitmask ^= num
        # bitmask是2个只出现1次的数的异或结果，代表了2者二进制位的差异

        # rightmost 1-bit diff between x and y
        diff = bitmask & (-bitmask)  # 可以保留bitmask最右边为1的位

        one_of_them = 0
        for num in nums:
            # bitmask which will contain only x
            # 通过循环排除掉出现2次的数
            if num & diff:
                one_of_them ^= num
        return [one_of_them, bitmask ^ one_of_them]

