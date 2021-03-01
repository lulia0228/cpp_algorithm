#--coding:utf-8--

class Solution:
    def swapNumbers(self, numbers: List[int]) -> List[int]:
        # 利用a^b^a=b
        numbers[0] = numbers[0]^numbers[1] # a^b
        numbers[1] = numbers[0]^numbers[1] # a^b^b
        numbers[0] = numbers[0]^numbers[1] # a^b^a^b^b
        return numbers
