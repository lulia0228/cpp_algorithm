# -*- coding: utf-8 -*-
# @Time    : 2020/9/19 16:04
# @Author  : Heng Li
# @File    : L395-m.py
# @Software: PyCharm

# 分治法
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        # 找到字符串出现次数最少的字符
        t = min(set(s), key=s.count)
        # 出现次数最少的字符的出现次数>=k
        if s.count(t) >= k:
            return len(s)
        return max(self.longestSubstring(a,k) for a in s.split(t))

# 这种更容易想到
# 滑窗 和常规意义的滑动窗口不太一样，窗口左端起点永远是0开始...
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        res = 0
        if len(s) < k:
            return 0
        record = {c: 0 for c in s}
        for rt in range(len(s)):
            record[s[rt]] += 1
            if rt >= k - 1 and record[s[rt]] >= k:
                # new_record = record # 是引用，仍然会修改掉原来record的值
                new_record = copy.deepcopy(record)
                max_cur_len = self.reduce_window(0, rt, new_record, s, k)
                res = max(res, max_cur_len)
        return res

    def reduce_window(self, lt, rt, new_record, s, k):
        ans = 0
        while rt - lt + 1 >= k:
            flag = 0
            for key, val in new_record.items():
                if val > 0 and val < k:
                    flag = 1
                    break
            if flag == 0:
                return max(ans, rt - lt + 1)
            new_record[s[lt]] -= 1
            lt += 1
        return ans
