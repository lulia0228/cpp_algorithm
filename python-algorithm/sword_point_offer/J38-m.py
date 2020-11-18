#--coding:utf-8--

# 这道剑指题 包含了存在重复字符的情况；类似leetcode 带有重复数字的全排列47

class Solution:
    def permutation(self, s: str) :
        res = []
        visited = [0] * len(s)
        s = "".join(sorted(list(s)))
        self.dfs(s, 0, "", res, visited)
        return res

    def dfs(self, s, idx, tmp, res, visited):
        if idx == len(s):
            res.append(tmp)
            return
        for i in range(len(s)):
            # 解决重复字符问题
            if i != 0 and s[i] == s[i - 1] and visited[i-1]:
                continue
            if not visited[i]:
                visited[i] = 1
                self.dfs(s, idx + 1, tmp + s[i], res, visited)
                visited[i] = 0


if __name__ == "__main__":
    s = "aab"
    # s = "abc"
    res = Solution().permutation(s)
    print(res)