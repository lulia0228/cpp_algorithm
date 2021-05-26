#--coding:utf-8--

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        sum_ = sum(arr)
        if sum_ % 3 != 0: return False
        t_sum , idx = 0, 0
        while idx < len(arr):
            t_sum += arr[idx]
            if t_sum == sum_//3:
                break
            idx += 1
        if t_sum != sum_//3: return False
        j = idx + 1
        while j+1 < len(arr):
            t_sum += arr[j]
            if t_sum == 2*sum_//3:
                return True
            j += 1
        return False


# 太慢
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        r_d = collections.defaultdict(list)
        sum_ = 0
        for idx,n in enumerate(arr):
            sum_ += n
            r_d[sum_].append(idx)
        if sum_%3 != 0 : return False
        target = sum_//3
        i_ls = r_d.get(target, [])
        j_ls = r_d.get(2*target, [])
        if not i_ls or not j_ls or i_ls[0]>=j_ls[-1]:
            return False
        if sum_ == 0:
            return False if len(r_d.get(0, []))< 3 else True
        return True
