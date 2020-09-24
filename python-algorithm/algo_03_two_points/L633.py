#--coding:utf-8--
'''
@Time   : 2020/9/24
@Author : Heng Li
@Email  : liheng_lulia@163.com
'''

# 题目只说是2个整数，没说不能是2个一样的整数
import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        lt = 0
        rt = int(math.sqrt(c))
        while lt <= rt:
            s = lt*lt +rt*rt
            if s > c:
                rt -= 1
            elif s < c:
                lt += 1
            else:
                return True
        return False