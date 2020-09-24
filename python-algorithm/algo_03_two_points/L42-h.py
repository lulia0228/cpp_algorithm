#--coding:utf-8--
'''
@Time   : 2020/8/13
@Author : Heng Li
@Email  : liheng@elensdata.com
'''

# 宽度为1，以每个柱子上可以装的水作为计算单元，只需知道它的左右两侧分别最高值，和二者中的较小值差值即为所求

class Solution:
    def trap(self, height: List[int]) -> int:
        sz = len(height)
        if sz < 3:
            return 0
        left, right = 0, sz-1
        l_max, r_max = height[0], height[sz-1]
        res = 0
        while left <= right:
            l_max = max(l_max, height[left])
            r_max = max(r_max, height[right])
            if l_max <= r_max:
                res += l_max - height[left]
                left += 1
            else:
                res += r_max - height[right]
                right -= 1
        return res

