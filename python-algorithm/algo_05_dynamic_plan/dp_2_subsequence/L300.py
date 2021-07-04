#--coding:utf-8--


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        final_max = 1
        # dp[i]表示以nums[i]为结尾的上升子序列的最大长度
        dp = [1]*len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
            final_max = max(final_max, dp[i])
        return final_max

# 上升子序列的结尾的数越小，那么遍历的时候后面接上一个数，
# 会有更大的可能构成一个长度更长的上升子序列。
# 定义新状态数组，tail[i] 表示：长度为 i+1 的 所有上升子序列的结尾的最小值。
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        (1)tail[i]最终表示的是长度为i+1的递增子序列中尾数最小的值；因此tail是递增的
        (2)在遍历时通过二分法确定元素应该被放到tail中的具体位置，因此时间复杂度是N*logN
        '''
        tail = []
        for nu in nums:
            # 使用二分查找法，在有序数组 tail 中
            # 找到第 1 个大于等于 nums[i] 的元素，尝试让那个元素更小
            lt, rt = 0, len(tail)
            while lt<rt:
                mid = lt + (rt-lt)//2
                if tail[mid]<nu:
                    lt = mid + 1
                else:
                    rt = mid
            if lt == len(tail):
                tail.append(nu)
            else:
                tail[lt] = nu
        return len(tail)
