# -*- coding: utf-8 -*-

class my_node:
    def __init__(self, *args, **kwargs):
        self.end = False
        self.record = {}

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = my_node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tmp = self.root
        for c in word:
            if c not in tmp.record:
                tmp.record[c] = my_node()
            # 这里容易写成if else 导致没往下一层下探
            tmp = tmp.record[c]
        tmp.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tmp = self.root
        for c in word:
            if c not in tmp.record:
                return False
            tmp = tmp.record[c]
        return tmp.end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tmp = self.root
        for c in prefix:
            if c not in tmp.record:
                return False
            tmp = tmp.record[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


# 练习
# 211. 添加与搜索单词 - 数据结构设计
# 212. 单词搜索 II
# 421. 数组中两个数的最大异或值


# 另一种写法
class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lookup = {}  # 字典的key是字母，值是树

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curnode = self.lookup
        for char in word:
            if char not in curnode:
                curnode[char] = Trie()
            curnode = curnode[char].lookup
        curnode["end"] = "#"

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curnode = self.lookup
        for char in word:
            if char in curnode:
                curnode = curnode[char].lookup
            else:
                return False
        res = curnode.get("end")
        return res == "#"

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curnode = self.lookup
        for char in prefix:
            if char in curnode:
                curnode = curnode[char].lookup
            else:
                return False
        return True

