# -*- coding: utf-8 -*-

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

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


# 或者下面这样写

class TrieNode:
    def __init__(self):
        self.lookup = {}
        self.end = False

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curnode = self.root
        for char in word:
            if char not in curnode.lookup:
                curnode.lookup[char] = TrieNode()
            curnode = curnode.lookup[char]
        curnode.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curnode = self.root
        for char in word:
            if char in curnode.lookup:
                curnode = curnode.lookup[char]
            else:
                return False
        return curnode.end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curnode = self.root
        for char in prefix:
            if char in curnode.lookup:
                curnode = curnode.lookup[char]
            else:
                return False
        return True

