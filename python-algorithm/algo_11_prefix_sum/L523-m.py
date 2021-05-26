#--coding:utf-8--

# 同余定理 同974
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        record = collections.defaultdict(list)
        record[0] = [-1]
        total, ans = 0, 0
        for idx, elem in enumerate(nums):
            total += elem
            modulus = total % k
            same_ls = record.get(modulus, [])
            if same_ls:
                if idx-same_ls[0]>1:
                    return True
            record[modulus].append(idx)
        return False

