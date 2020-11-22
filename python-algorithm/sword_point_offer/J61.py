#--coding:utf-8--


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        record = set()
        ma, mi = 0, 14
        for n in nums:
            if n == 0:
                continue
            if n in record:
                return False
            ma = max(ma, n)
            mi = min(mi, n)
            record.add(n)
        return True if ma-mi<5 else False
