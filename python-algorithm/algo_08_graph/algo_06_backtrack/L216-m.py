#--coding:utf-8--


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candinates = [i for i in range(1,10)] # 值是1-9
        res = []
        self.dfs(candinates, 0, k, n, [], res)
        return res

    def dfs(self, candinates, idx, k, n, cur_ls, res):
        if len(cur_ls) == k:
            if n == 0:
                res.append(cur_ls[:])
            return
        # if n < 0:
            # return
        for i in range(idx, 9): # candinates的索引是0-8
            # 因为candinates是1-9，单调递增.所以可以在这里剪枝
            if n < 0:
                break
            cur_ls.append(candinates[i])
            self.dfs(candinates, i+1, k, n-candinates[i], cur_ls, res)
            cur_ls.pop()