#--coding:utf-8--

class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = [int(n) for n in str(num)]
        num_dict = collections.defaultdict(int)
        for k,v in enumerate(nums):
            num_dict[v] = k

        for i in range(len(nums)-1):  #从索引0开始往后遍历到最后一位的前一位
            for n in range(9,nums[i],-1):    #从9开始一直遍历到比索引对应的数字大1为止
                if num_dict[n] > i:          #如果字典中这个数字存在且索引比一开始遍历的索引大，就更新数组。
                    nums[i] , nums[num_dict[n]] = nums[num_dict[n]] , nums[i]
                    return int("".join(str(n) for n in nums))
        return num


