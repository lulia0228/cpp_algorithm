#--coding:utf-8--

class Solution:

    def __init__(self, nums: List[int]):
        self.origin = nums[:]  # 避免2个数组地址一样，在shuffle时候产生影响
        self.copy = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.copy = self.origin
        self.origin = self.origin[:]  # 避免地址一样，在shuffle时候被影响
        return self.origin

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        # 洗牌算法
        for i in range(len(self.copy)):
            idx = random.randint(i, len(self.copy) - 1)
            self.copy[i], self.copy[idx] = self.copy[idx], self.copy[i]
        return self.copy

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()