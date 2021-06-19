
'''正数的反码和补码都与原码相同。
而负数的反码为对该数的原码除符号位外各位取反。
负数的补码为对该数的原码除符号位外各位取反，然后在最后一位加1

注意：计算机中负数是以补码形式储存的'''

class Solution:
    def FindNumsAppearOnce(self , nums ):
        # write code here
        # difference between two numbers (x and y) which were seen only once
        bitmask = 0
        # 异或，相同为0，不同为1
        for num in nums:
            bitmask ^= num
        # bitmask是2个只出现1次的数的异或结果，代表了2者二进制位的差异

        # rightmost 1-bit diff between x and y
        # 即找出2者的一个差异位
        diff = bitmask & (-bitmask)  # 可以保留bitmask最右边为1的位

        one_of_them = 0
        for num in nums:
            # bitmask which will contain only x
            # 通过循环排除掉出现2次的数
            if num & diff:
                one_of_them ^= num
        return [min(one_of_them, bitmask ^ one_of_them),
               max(one_of_them, bitmask ^ one_of_them)]