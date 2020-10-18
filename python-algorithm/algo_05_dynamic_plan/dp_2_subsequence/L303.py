#--coding:utf-8--


class NumArray:

    def __init__(self, nums: List[int]):
        self.s = []
        tmp = 0
        for i in range(len(nums)):
            tmp += nums[i]
            self.s.append(tmp)

    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.s[j]
        else:
            return self.s[j]-self.s[i-1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)