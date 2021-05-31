#--coding:utf-8--

# 缩小到一定范围后，再用的DFS 比较蠢 但是时间能过  和官方的也不一样
from functools import reduce
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        if n < 2: return str(n)
        res = ""
        new_n, new_k = n, k
        candinate = [i for i in range(1, n + 1)]
        last_k = new_k
        while new_k:
            tmp = reduce(lambda x, y: x * y, range(1, new_n))
            idx = new_k // tmp
            last_k = new_k
            new_k = new_k % tmp
            new_n -= 1
            if new_k:
                res += str(candinate[idx])
                candinate.pop(idx)

        record = []
        visited = [False for i in range(len(candinate))]
        self.dfs(candinate, 0, visited, [], record)
        t_s = "".join([str(item) for item in record[last_k-1]])
        res += t_s

        return res

    def dfs(self, candinates, idx, visited, cur_ls, record):
        if idx == len(candinates):
            record.append(cur_ls[:])
            return
        for i in range(len(candinates)):
            if not visited[i]:
                cur_ls.append(candinates[i])
                visited[i] = True
                self.dfs(candinates, idx+1, visited, cur_ls, record)
                cur_ls.pop()
                visited[i] = False


if __name__ == "__main__":
    n,k = 4, 9
    print(Solution().getPermutation(n,k))




# 纯暴力超时
class Solution1:
    def __init__(self, **kwargs):
        self.res = []
        self.flag = []
        self.cnt = 0

    def getPermutation(self, n: int, k: int) -> str:
        if nums == []:
            return self.res
        self.flag = [False for i in range(len(nums))]
        self.dfs(nums, 0, k, [])
        return self.res

    def dfs(self, candinates, idx, k, cur_ls):
        if self.cnt > k: return

        if idx == len(candinates):
            self.cnt += 1
            if self.cnt == k:
                self.res = cur_ls[:]
            return

        for i in range(len(candinates)):
            if not self.flag[i]:
                cur_ls.append(candinates[i])
                self.flag[i] = True
                self.dfs(candinates, idx + 1, k, cur_ls)
                cur_ls.pop()
                self.flag[i] = False