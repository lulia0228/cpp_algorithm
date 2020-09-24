#--coding:utf-8--
'''
@Time   : 2020/9/24
@Author : Heng Li
@Email  : liheng_lulia@163.com
'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lt, rt = 0, len(numbers)-1
        while lt < rt:
            s = numbers[lt] + numbers[rt]
            if s < target:
                lt += 1
            elif s > target:
                rt -= 1
            else:
                return [lt+1, rt+1]
        return []