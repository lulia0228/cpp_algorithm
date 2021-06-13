# -*- coding:utf-8 -*-

# 旋转数组的最小数字
# 牛客上此题未考虑是从重复数字处旋转的情况例如3 3 1 3
# 同lc154相同 ; lc153的升级版本

# 和lc33 lc81在旋转数组中搜索target有区别

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        lt, rt = 0, len(rotateArray) - 1
        if rotateArray[0] < rotateArray[rt]:
            return rotateArray[0]
        else:
            # 存在从重复数字处旋转的情况，需要将后面的重复数字用rt更新掉
            if rotateArray[0] == rotateArray[rt]:
                while lt<rt and rotateArray[rt] == rotateArray[-1]:
                    rt -= 1
            while lt < rt:
                mid = lt + (rt - lt) // 2
                # 这里只能和右端点rt比，不能使用左端点lt（后半段无法根据lt判断方向）
                if rotateArray[mid] <= rotateArray[rt]:
                    rt = mid
                else:
                    lt = mid + 1

        return rotateArray[lt]