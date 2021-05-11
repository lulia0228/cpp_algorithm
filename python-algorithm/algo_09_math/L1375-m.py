#--coding:utf-8--

#  核心：当前已亮灯泡编号的最大值 == 当前已亮灯泡的个数 时，就是全蓝。
class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        cnt = 0
        max_turned_on = -float("inf")
        for idx, bulb in enumerate(light):
            max_turned_on = max(max_turned_on, bulb)
            if idx+1 == max_turned_on:
                cnt += 1
        return cnt


# 笨方法
class Solution1:
    def numTimesAllBlue(self, light: List[int]) -> int:

        def all_blue_cur(flag):
            if flag[0] != 1:
                return False
            last = 0
            for idx, itm in enumerate(flag):
                if idx != 0 and itm == 1:
                    if idx - last != 1:
                        return False
                    last = idx
            return True

        flag = [0] * len(light)
        cnt = 0
        for idx, bulb in enumerate(light):
            flag[bulb - 1] = 1
            if all_blue_cur(flag):
                cnt += 1
        return cnt