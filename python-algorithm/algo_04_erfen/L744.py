#--coding:utf-8--

# 找到第一个比目标值大的元素

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if letters[-1] <= target:
            return letters[0]
        lt, rt = 0, len(letters)-1
        while lt < rt:
            mid = lt + (rt-lt)//2
            if letters[mid] <= target:
                lt = mid + 1
            else:
                rt = mid
        return letters[lt]


# 找到第一个比目标值大的元素
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if letters[-1] <= target:
            return letters[0]
        lt, rt = 0, len(letters)-1
        while lt <= rt:
            mid = lt + (rt-lt)//2
            if letters[mid] <= target:
                lt = mid + 1
            else:
                rt = mid - 1
        if lt < len(letters):
            return letters[lt]
        return ""