#--coding:utf-8--

#  有点类似快排的思想
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        new_nums = nums
        lt, rt = 0, len(new_nums)-1
        while lt < rt:
            # 不能少了lt<rt条件；找第一个偶数
            while lt<rt and new_nums[lt]&1:
                lt += 1
            # 不能少了lt<rt条件；找第一个奇数
            while lt<rt and new_nums[rt]&1==0:
                rt -= 1
            new_nums[lt], new_nums[rt] = new_nums[rt], new_nums[lt]
            # 交换后，2个指针都不要忘记更新
            lt += 1
            rt -= 1
        return new_nums