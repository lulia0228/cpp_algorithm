#
#
# @param arr int整型一维数组 the array
# @return int整型
#

# 滑动窗口的思想

class Solution:
    def maxLength(self, arr):
        # write code here
        r_d = {}
        res = 1
        i, j = 0, 0
        while j < len(arr):
            if arr[j] not in r_d:
                r_d[arr[j]] = 1
            else:
                r_d[arr[j]] += 1
            while r_d[arr[j]] > 1:
                r_d[arr[i]] -= 1
                i += 1  # 注意顺序不要反了，先让窗口左侧收缩掉的元素 记录-1
            res = max(res, j - i + 1)
            j += 1
        return res
