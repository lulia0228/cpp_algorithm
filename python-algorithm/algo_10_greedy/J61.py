#--coding:utf-8--
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        st = set()
        min_val = float("inf")
        max_val = -float("inf")
        for n in nums:
            if n != 0:
                min_val = min(min_val, n)
                max_val = max(max_val, n)
                if n in st:
                    return False
                st.add(n)
        return max_val-min_val<5

