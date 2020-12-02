#--coding:utf-8--


class Solution:
    max_split = 1
    def maxUniqueSplit(self, s: str) -> int:
        lenth = len(s)
        st = set()
        self.dfs(s, 0, 0, st)
        return self.max_split

    def dfs(self, s, start, split, st):
        if start == len(s):
            self.max_split = max(self.max_split, split)
            return
        for i in range(start, len(s)):
            tmp_str = s[start:i+1]
            if tmp_str not in st:
                st.add(tmp_str)
                # 是i+1,不是start+1
                self.dfs(s, i+1, split+1, st)
                st.remove(tmp_str)

