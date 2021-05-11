#--coding:utf-8--

# 10叉树先序遍历
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:

        def dfs(rec, i, n):
            if i > n:
                return -1
            rec.append(i);
            child = i * 10
            for j in range(10):
                if dfs(rec, child+j, n) == -1: break
            return

        rec = []
        for i in range(1, 10):
            dfs(rec, i, n)
        return rec