#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param nums int整型一维数组
# @param target int整型
# @return int整型
#

# 注意也可以和nums[0]比较来判断 target和mid在左子数组还是右子数组中
# 这里选择和nums[-1]比较
# 本题同lc33 lc81（升级版本）


class Solution:
    def search(self, nums, target):
        # write code here
        lt, rt = 0, len(nums) - 1
        while lt <= rt:
            mid = lt + (rt - lt) // 2
            if target > nums[-1]:  # 目标在左子数组
                if nums[mid] < nums[-1]:  # 中点在右子数组
                    rt = mid - 1
                else:
                    if nums[mid] > target:
                        rt = mid - 1
                    elif nums[mid] < target:
                        lt = mid + 1
                    else:
                        return mid
            else:  # 目标在右子数组
                if nums[mid] > nums[-1]:  # 中点在左子数组
                    lt = mid + 1
                else:
                    if nums[mid] > target:
                        rt = mid - 1
                    elif nums[mid] < target:
                        lt = mid + 1
                    else:
                        return mid
        return -1
