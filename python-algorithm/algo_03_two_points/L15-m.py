#--coding:utf-8--


# 注意两处去重
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) < 3: return res
        nums.sort()
        for i in range(len(nums)-2):
            if nums[i] > 0: break
            # 第一处去重，防止起始值重复
            if i>0 and nums[i] == nums[i-1]: continue
            lt, rt = i+1, len(nums)-1
            while lt<rt:
                tmp = nums[lt]+nums[rt]
                if tmp == -nums[i]:
                    res.append([nums[i], nums[lt], nums[rt]])
                    lt += 1
                    rt -= 1
                    # 第二处去重，防止第2，3个数组合重复
                    while lt < rt and nums[lt]==nums[lt-1]:
                        lt += 1
                    while lt < rt and nums[rt]==nums[rt+1]:
                        rt-=1
                elif tmp > -nums[i]:
                    rt -= 1
                else:
                    lt += 1
        return res




