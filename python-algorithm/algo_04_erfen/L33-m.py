#--coding:utf-8--

# 先判断target在左子数组还是右子数组
# 在判断中点在左子数组还是右子数组

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lt, rt = 0, len(nums)-1
        while lt <= rt: # 必须是等号
            mid = lt + (rt-lt)//2
            if nums[0] > target: # 目标在右子数组
                if nums[mid] >= nums[0]: # 中点在左子数组
                    lt = mid + 1
                else: # 中点在右子数组
                    if nums[mid] == target:
                        return mid
                    elif nums[mid] > target:
                        rt = mid-1
                    else:
                        lt = mid + 1
            else: # 目标在左子数组
                if nums[mid] < nums[0]: # 中点在左子数组
                    rt = mid - 1
                else: # 中点在右子数组
                    if nums[mid] == target:
                        return mid
                    elif nums[mid] > target:
                        rt = mid - 1
                    else:
                        lt = mid + 1
        return -1






