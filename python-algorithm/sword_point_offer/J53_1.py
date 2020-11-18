#--coding:utf-8--


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 找到最后出现的位置
        def findT(nums, target):
            lt, rt = 0, len(nums)-1
            while lt <= rt:
                mid = lt + (rt-lt)//2
                if nums[mid] > target:
                    rt = mid-1
                else:
                    lt = mid+1
            if rt >=0 and nums[rt] == target:
                return rt
            return -1

        flag = findT(nums, target)
        if flag == -1:
            return 0
        else:
            cnt = 0
            idx = flag
            while idx>=0 and nums[idx] == nums[flag]:
                cnt += 1
                idx -= 1
        return cnt

