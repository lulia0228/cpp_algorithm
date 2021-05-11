#--coding:utf-8--
class Solution:

    def __init__(self, A: List[int]):
        self.pre = [A[0]]
        for i in range(1, len(A)):
            self.pre.append(self.pre[-1] + A[i])

    # 查找第一个大于目标值的2种写法

    def pickIndex(self) -> int:
        # 随机生成一个数；题目说了是正整数数组；即落在pre[i]-A[i]内的数字被映射到同一个下标
        rd = int(random.random() * self.pre[-1])
        l, r = 0, len(self.pre) - 1
        while l < r:
            mid = (l + r) // 2
            # 找到第一个大于rd的下标
            if self.pre[mid] > rd:
                r = mid
            else:
                l = mid + 1
        return l


    # def pickIndex(self) -> int:
    #     # 随机生成一个数
    #     rd = int(random.random() * self.pre[-1])
    #     l, r = 0, len(self.pre) - 1
    #     while l <= r:
    #         mid = (l + r) // 2
    #         # 找到第一个大于rd的下标
    #         if self.pre[mid] <= rd:
    #             l = mid + 1
    #         else:
    #             r = mid - 1
    #     return l



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()