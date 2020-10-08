# -*- coding: utf-8 -*-
# @Time    : 2020/10/7 12:44
# @Author  : No Name

# 题目描述：不考虑二进制表示中的首 0 部分。
# 对于 00000101，要求补码可以将它与 00000111 进行异或操作。那么问题就转换为求掩码 00000111。
# 首先知道1^1=0 1^0=1
# 那么求反就是原数字和一堆1异或即可（因为没有前导零位）
# 例如5取反 就是 101^111=010
# 所以思路就是先找到它占了多少位，然后和这么多位的1求异或即可

class Solution:
    def findComplement(self, num: int) -> int:
        cnt = 1
        c = num
        while c != 1:
            cnt += 1
            c >> 1
        tmp = 2**cnt-1
        return tmp^num