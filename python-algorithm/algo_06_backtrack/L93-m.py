#--coding:utf-8--

# 对于此类问题，要搞明白每层循环的候选对象到底是什么！！！
from typing import *
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        self.dfs(s, 0, [], res)
        return res

    def dfs(self, s, idx, tmp, res):
        if len(tmp) == 4:
            if idx == len(s):
                res.append(".".join(tmp))
            return
        for i in range(1, 4):
            # 过滤掉越界的情况
            if idx + i > len(s):
                continue
            t_str = s[idx:idx + i]
            # i==1 是为了处理特殊情况0.0.0.0
            if i == 1 or (int(t_str) <= 255 and s[idx] != "0"):
                tmp.append(t_str)
                self.dfs(s, idx + i, tmp, res)
                tmp.pop()

if __name__ == "__main__":
    str1 = "1111"
    ip = Solution().restoreIpAddresses(str1)
    print(ip)