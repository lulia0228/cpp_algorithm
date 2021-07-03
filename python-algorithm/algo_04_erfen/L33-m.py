#--coding:utf-8--

# 先判断target在左子数组还是右子数组
# 在判断中点在左子数组还是右子数组

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        sz = len(nums)
        lt, rt = 0, sz-1
        while lt<=rt:
            mid = lt + (rt-lt)//2
            if nums[0]>target: # 目标在右子数组
                if nums[0]<=nums[mid]: # 中点在左子数组
                    lt = mid+1
                else:
                    if nums[mid]>target:
                        rt = mid-1
                    elif nums[mid]<target:
                        lt = mid+1
                    else:
                        return mid
            else: # 目标在左子数组
                if nums[0]>nums[mid]: # 中点在右子数组
                    rt = mid-1
                else:
                    if nums[mid]>target:
                        rt = mid-1
                    elif nums[mid]<target:
                        lt = mid+1
                    else:
                        return mid
        return -1







