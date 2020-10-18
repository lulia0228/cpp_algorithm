#--coding:utf-8--


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        sz = len(nums)
        min_sum = inf
        res = 0
        for i in range(sz):
            # 去掉以相同值开始的重复情况
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            lt, rt = i + 1, sz - 1
            while lt < rt:
                s = nums[i] + nums[lt] + nums[rt] - target
                if abs(s) < min_sum:
                    min_sum = abs(s)
                    res = s + target
                if s > 0:
                    rt -= 1
                    while lt < rt and nums[rt] == nums[rt + 1]:  # 可以拿掉这段
                        rt -= 1
                elif s < 0:
                    lt += 1
                    while lt < rt and nums[lt] == nums[lt - 1]:  # 可以拿掉这段
                        lt += 1
                else:
                    return s + target
        return res
