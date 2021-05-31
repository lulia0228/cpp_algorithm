#--coding:utf-8--

class Solution:
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        record = [[] for i in range(n)]
        for item in graph:
            record[item[0]].append(item[1])
        if self.dfs(record, start, target):
            return True
        return False

    def dfs(self, record, start, end):
        if start == end: return True
        for next in record[start]:
            if self.dfs(record, next, end):
                return True
        return False
