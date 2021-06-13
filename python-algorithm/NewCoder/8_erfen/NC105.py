#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 如果目标值存在返回下标，否则返回 -1
# @param nums int整型一维数组
# @param target int整型
# @return int整型
#

# 第一个出现的目标

class Solution:
    def search(self , nums , target ):
        # write code here
        if not nums: return -1
        lt, rt = 0, len(nums)-1
        while lt < rt:
            mid = lt +(rt-lt)//2
            if nums[mid] >= target:
                rt = mid
            else:
                lt = mid+1
        return lt if nums[lt]==target else -1