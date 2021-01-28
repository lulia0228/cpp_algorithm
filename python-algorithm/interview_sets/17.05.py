#--coding:utf-8--
class Solution:
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        sz = len(array)
        sum_ = 0
        record = dict()
        record[0] = -1  #
        max_len, max_start = 0, -1
        for i in range(sz):
            if "A" <= array[i] <= "Z" or "a" <= array[i] <= "z":
                sum_ += 1
            else:
                sum_ -= 1
            if sum_ in record:
                if i - record[sum_] > max_len:
                    max_len = i - record[sum_]
                    max_start = record[sum_]
            else:
                record[sum_] = i
        return array[max_start + 1:max_start + 1 + max_len]




