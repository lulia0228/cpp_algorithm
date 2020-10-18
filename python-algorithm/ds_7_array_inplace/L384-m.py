# -*- coding: utf-8 -*-


# Fisher-Yates 洗牌算法跟暴力算法很像。在每次迭代中，
# 生成一个范围在当前下标到数组末尾元素下标之间的随机整数。
# 接下来，将当前元素和随机选出的下标所指的元素互相交换

class Solution:
    def __init__(self, nums: List[int]):
        self.origin = nums[:]  # 避免2个数组地址一样，在shuffle时候产生影响
        self.copy = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.copy = self.origin  # copy数组也要被复位吗？
        self.origin = self.origin[:]  # 避免地址一样，在shuffle时候被影响
        return self.origin

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        for i in range(len(self.copy)):
            idx = random.randint(i, len(self.copy) - 1)
            self.copy[i], self.copy[idx] = self.copy[idx], self.copy[i]
        return self.copy

        # Your Solution object will be instantiated and called as such:
        # obj = Solution(nums)
        # param_1 = obj.reset()
        # param_2 = obj.shuffle()