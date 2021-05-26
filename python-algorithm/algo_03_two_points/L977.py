#--coding:utf-8--
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        lt, rt = 0, len(nums)-1
        res = [0 for i in range(len(nums))]
        idx = -1
        while lt < rt:
            t1, t2 = pow(nums[lt],2), pow(nums[rt], 2)
            if t1 < t2:
                res[idx] = t2
                rt -= 1
            elif t1 > t2:
                res[idx] = t1
                lt += 1
            else:
                res[idx] = t1
                idx -= 1
                res[idx] = t2
                lt += 1
                rt -= 1
            idx -= 1

        if lt == rt:
            res[0] = pow(nums[lt],2)
        return res

