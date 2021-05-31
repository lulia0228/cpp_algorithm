#--coding:utf-8--
class Solution:
    def pairSums(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        st = dict()
        for num in nums:
            tmp = target-num
            if  tmp in st and st[tmp]>0:
                res.append([tmp, num])
                st[tmp] -= 1
            else:
                if num not in st:
                    st[num] = 1
                else:
                    st[num] += 1
        return res