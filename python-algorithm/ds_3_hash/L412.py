# -*- coding: utf-8 -*-
# @Time    : 2020/10/1 18:22
# @Author  : Heng Li
# @File    : L412.py
# @Software: PyCharm

# 这道题写这么麻烦，用到了哈希表，主要是为了通用性，如果游戏扩大：
# 能被7整除只需要加上一行 record.update(7: "Jazz") ,比手动写条件判断可轻松多了

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        record = {
            3:"Fizz",
            5:"Buzz"
        }
        res = []
        for i in range(1, n+1):
            tmp_str = ""
            for k,v in record.items():
                if i%k == 0:
                    tmp_str += v
            if tmp_str == "":
                res.append(str(i))
            else:
                res.append(tmp_str)
        return res