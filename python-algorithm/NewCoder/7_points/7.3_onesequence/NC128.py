#
# max water
# @param arr int整型一维数组 the array
# @return long长整型
#

# 同lc 42 接雨水

class Solution:
    def maxWater(self , arr ):
        # write code here
        sz = len(arr)
        if sz < 3: return 0
        left, right = 0, sz-1
        l_max, r_max = arr[0], arr[sz-1]
        res = 0
        while left <= right:
            l_max = max(l_max, arr[left]);
            r_max = max(r_max, arr[right]);
            if l_max <= r_max:
                res += l_max - arr[left]
                left += 1
            else:
                res += r_max - arr[right]
                right -= 1
        return res

# [3,1,2,5,2,4]