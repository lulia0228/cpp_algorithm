#--coding:utf-8--
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        lt, rt = 0, len(nums) - 1
        # 相比lc33多的代码段
        if nums[0] == nums[-1]:
            while lt < rt and nums[rt] == nums[-1]:
                rt -= 1
        while lt <= rt:
            mid = lt + (rt - lt) // 2
            if nums[0] > target:  # 目标在右子数组
                if nums[mid] >= nums[0]:  # 中点在左子数组
                    lt = mid + 1
                else:  # 中点在右子数组
                    if nums[mid] == target:
                        return True
                    elif nums[mid] > target:
                        rt = mid - 1
                    else:
                        lt = mid + 1
            else:  # 目标在左子数组
                if nums[mid] < nums[0]:  # 中点在左子数组
                    rt = mid - 1
                else:  # 中点在右子数组
                    if nums[mid] == target:
                        return True
                    elif nums[mid] > target:
                        rt = mid - 1
                    else:
                        lt = mid + 1
        return False



