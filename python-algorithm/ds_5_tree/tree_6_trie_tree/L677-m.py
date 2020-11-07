# -*- coding: utf-8 -*-

class TrieNode:

    def __init__(self):
        self.val = 0
        self.children = {}
        self.end = False

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        curnode = self.root
        for char in key:
            if char not in curnode.children:
                curnode.children[char] = TrieNode()
            curnode = curnode.children[char]
        curnode.val = val
        curnode.end = True

    # 递归加和
    def dfs(self, root):
        res = 0
        if root.end:
            res += root.val
        for child, node in root.children.items():
            res += self.dfs(node)
        return res

    # 查询是否存在前缀
    def sum(self, prefix: str) -> int:
        curnode = self.root
        for char in prefix:
            if char in curnode.children:
                curnode = curnode.children[char]
            else:
                return 0
        return self.dfs(curnode)

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)