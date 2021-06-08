#--coding:utf-8--
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param nums int一维数组
# @return int二维数组
#

class Solution:
    def foundMonotoneStack(self, nums):
        # write code here
        sz = len(nums)
        res = [[-1, -1] for _ in range(sz)]
        stk = [0]
        for i in range(1, sz):
            while stk and nums[stk[-1]] > nums[i]:
                idx = stk.pop(-1)
                res[idx][1] = i
            stk.append(i)
        stk = [sz - 1]
        for i in range(sz - 2, -1, -1):
            while stk and nums[stk[-1]] > nums[i]:
                idx = stk.pop(-1)
                res[idx][0] = i
            stk.append(i)
        return res
