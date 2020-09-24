#--coding:utf-8--
'''
@Time   : 2020/9/22
@Author : Heng Li
@Email  : liheng_lulia@163.com
'''
# 这道题的证明...
class Solution:
    def maxArea(self, height: List[int]) -> int:
        lt, rt = 0, len(height)-1
        res = 0
        while lt < rt:
            res = max(res, min(height[lt], height[rt])*(rt-lt))
            if height[lt]<height[rt]:
                lt += 1
            else :
                rt -= 1
        return res