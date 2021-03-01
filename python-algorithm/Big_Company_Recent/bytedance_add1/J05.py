# -*- coding: utf-8 -*-
# leetcode submit region begin(Prohibit modification and deletion)
# 字符数组解
class Solution:
    def replaceSpace(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            if s[i] == ' ':
                res += "%20"
            else:
                res += s[i]
        return res
# leetcode submit region end(Prohibit modification and deletion)