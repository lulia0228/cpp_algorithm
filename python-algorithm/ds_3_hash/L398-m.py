#--coding:utf-8--


# 随机数索引
class Solution:

    def __init__(self, nums: List[int]):
        self.r_d = collections.defaultdict(list)
        for idx, val in enumerate(nums):
            self.r_d[val].append(idx)


    def pick(self, target: int) -> int:
        idx = random.randint(0, sys.maxsize)%len(self.r_d[target])
        return self.r_d[target][idx]


# 蓄水池采样
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums


    def pick(self, target: int) -> int:
        cnt, idx = 0, 0
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                cnt += 1
                if random.randint(0, sys.maxsize)%cnt == 0:
                    idx = i
        return idx