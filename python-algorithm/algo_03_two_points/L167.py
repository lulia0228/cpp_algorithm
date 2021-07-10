#--coding:utf-8--

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            low, high = i + 1, n - 1
            while low <= high:
                mid = low+(high-low)//2
                if numbers[mid] == target - numbers[i]:
                    return [i + 1, mid + 1]
                elif numbers[mid] > target - numbers[i]:
                    high = mid - 1
                else:
                    low = mid + 1
        return [-1, -1]


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lt, rt = 0, len(numbers)-1
        while lt < rt:
            s = numbers[lt] + numbers[rt]
            if s < target:
                lt += 1
            elif s > target:
                rt -= 1
            else:
                return [lt+1, rt+1]
        return [-1, -1]