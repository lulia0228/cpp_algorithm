#--coding:utf-8--

class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        res = []
        i = j = 1
        tmp_sum = 0
        tmp_ls = []
        while j <= target//2+1:
            tmp_sum += j
            tmp_ls.append(j)
            while tmp_sum >= target:
                if tmp_sum == target:
                    res.append(tmp_ls[:])
                tmp_sum -= i
                tmp_ls.pop(0)
                i += 1
            j += 1
        return res
