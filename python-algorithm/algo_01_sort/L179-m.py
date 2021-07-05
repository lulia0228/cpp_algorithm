#--coding:utf-8--
# 179. 最大数
from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(m, n):
            s1 = str(m)+str(n)
            s2 = str(n)+str(m)
            if int(s1)>int(s2):
                return -1
            elif int(s1)<int(s2):
                return 1
            else:
                return 0
        # 从大到小排序
        nums.sort(key = cmp_to_key(cmp))
        res = "".join([str(it) for it in nums])
        # 处理[0, 0]特殊情况
        return  res if int(res) else "0"