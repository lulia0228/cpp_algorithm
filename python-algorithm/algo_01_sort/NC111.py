#--coding:utf-8--

import functools
class Solution:
    def solve(self, nums):
        # write code here
        new_nums = sorted(nums, key=functools.cmp_to_key(self.func), reverse=True)
        if new_nums[0] == 0:
            return "0"
        return "".join([str(item) for item in new_nums])

    def func(self, x, y):
        if int(str(x) + str(y)) > int(str(y) + str(x)):
            return 1
        else:
            return -1