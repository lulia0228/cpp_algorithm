#
#
# @param num int整型一维数组
# @return int整型二维数组
#

class Solution:
    def threeSum(self, num):
        # write code here
        res = []
        sz = len(num)
        if sz < 3: return res
        num.sort()
        if num[0] > 0: return res
        for i in range(sz - 2):
            # 避免起始值重复的情况
            if i > 0 and num[i] == num[i - 1]:
                continue
            lt, rt = i + 1, sz - 1
            while lt < rt:
                if num[lt] + num[rt] == -num[i]:
                    res.append([num[i], num[lt], num[rt]])
                    tmp1, tmp2 = num[lt], num[rt]
                    # 避免中间值重复
                    while lt < sz and num[lt] == tmp1:
                        lt += 1
                    while rt >= 0 and num[rt] == tmp2:
                        rt -= 1
                elif num[lt] + num[rt] > -num[i]:
                    rt -= 1
                else:
                    lt += 1
        return res



