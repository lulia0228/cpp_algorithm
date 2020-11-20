#--coding:utf-8--


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        bitmask = 0
        for num in nums:
            bitmask ^= num
        diff = bitmask & (-bitmask)
        one_of_them = 0
        for num in nums:
            if num & diff :
                one_of_them ^= num
        return [one_of_them, one_of_them^bitmask]

