#--coding:utf-8--
#
#
# @param operators string字符串二维数组 the ops
# @return string字符串一维数组
#

class TrieNode:
    def __init__(self):
        self.cnt = 1
        self.flag = False
        self.children = {}

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def trieU(self, operators):
        # write code here
        res = []
        for ops in operators:
            if ops[0] == "1":
                self.insert(ops[1])
            elif ops[0] == "2":
                self.delete(ops[1])
            elif ops[0] == "3":
                if self.search(ops[1]):
                    res.append("YES")
                else:
                    res.append("NO")
            elif ops[0] == "4":
                cnt = self.prefixNumber(ops[1])
                res.append(str(cnt))
        return res

    def insert(self, word):
        head = self.root
        for char in word:
            if char not in head.children:
                head.children[char] = TrieNode()
            else:
                head.children[char].cnt += 1
            head = head.children[char]
        head.flag = True

    def delete(self, word):
        head = self.root
        for char in word:
            head.children[char].cnt -= 1
            head = head.children[char]

    def search(self, word):
        head = self.root
        for char in word:
            if char not in head.children:
                return False
            head = head.children[char]
        return head.flag and head.cnt > 0

    def prefixNumber(self, word):
        head = self.root
        for char in word:
            if char not in head.children:
                return 0
            head = head.children[char]
        return head.cnt

ops = [["1","qwer"],["1","qwe"],["3","qwer"],["4","q"],
       ["2","qwer"],["3","qwer"],["4","q"]]

res = Solution().trieU(ops)
print(res)