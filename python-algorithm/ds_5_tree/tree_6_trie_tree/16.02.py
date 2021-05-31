#--coding:utf-8--
class WordsFrequency:

    def __init__(self, book: List[str]):
        self.my_tree = Trie()
        for word in book:
            self.my_tree.insert(word)

    def get(self, word: str) -> int:
        return self.my_tree.search(word)

class TrieNode:
    def __init__(self):
        self.lookup = {}
        self.end = False
        self.count = 0

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
        curnode.count +=  1

    def search(self, word: str) -> bool:
            """
            Returns if the word is in the trie.
            """
            curnode = self.root
            for char in word:
                if char in curnode.lookup:
                    curnode = curnode.lookup[char]
                else:
                    return 0
            if curnode.end:
                return curnode.count
            return 0

# Your WordsFrequency object will be instantiated and called as such:
# obj = WordsFrequency(book)
# param_1 = obj.get(word)