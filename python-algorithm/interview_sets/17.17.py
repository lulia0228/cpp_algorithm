#--coding:utf-8--
class wordTree():
    def __init__(self,val):
        self.val = val #字母的值
        self.nextnode = dict()#他的子节点用字典存储，方便获取和查询
        self.end = False #树中的一个单词的结尾，结尾处置True
        self.id = -1 #这个单词所在列表的位置，用于在这个位置添加索引
class Solution(object):
    def multiSearch(self, big, smalls):
        """
        :type big: str
        :type smalls: List[str]
        :rtype: List[List[int]]
        """
        size = len(big)

        ####
        #根据给的字典列表创建整个树，将节点不断插入到树中，前缀相同的话就往下层插入
        ####
        head = wordTree('#')
        for i,word in enumerate(smalls):
            curnode = head
            for w in word:
                if w not in curnode.nextnode: #如果该节点没有在子节点中
                    curnode.nextnode[w]=wordTree(w) #创建节点分支
                    curnode = curnode.nextnode[w] #指针指向该分支
                else:
                    curnode = curnode.nextnode[w] #向子节点深入
            curnode.end=True #一个单词完事了，在该叶子节点加上标记True
            curnode.id = i #加上该单词的索引位置，id


        #从头到尾遍历以每个字符为起始情况能够匹配多少树枝
        res = [[] for i in range(len(smalls))]
        for i,ch in enumerate(big):
            index = i #得到一个匹配位置
            curnode=head #将指针指向根节点
            while True: #往后循环
                if index>=size or big[index] not in curnode.nextnode: #如果指针所指向的字母不在子节点列表里面 或者指针越界者break
                    break
                curnode = curnode.nextnode[big[index]]#如果在往下一层匹配
                if curnode.end:#如果匹配到一个单词的末尾
                    res[curnode.id].append(i)#获取该单词的位置，并将起始位置加入搭配这个单词的匹配列表里面
                    index+=1
                else:
                    index+=1
        return res


# 慢
class Solution1:
    def multiSearch(self, big: str, smalls: List[str]) -> List[List[int]]:
        my_trie = Trie()
        res = [[] for i in range(len(smalls))]
        smll_idx = {w: i for i, w in enumerate(smalls)}
        for w in smalls:
            my_trie.insert(w)
        for i in range(len(big)):
            tmp_ls = my_trie.find_starts(big[i])
            # print(i, big[i], tmp_ls)
            if tmp_ls != []:
                for w in tmp_ls:
                    if i + len(w) <= len(big) and big[i:i + len(w)] == w:
                        res[smll_idx[w]].append(i)
        return res


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

    def find_starts(self, char):

        def dfs(root, tmp_str, res):
            if root.end:
                res.append(tmp_str)
            for node in root.lookup:
                dfs(root.lookup[node], tmp_str + node, res)

        curnode = self.root
        res = []
        if char not in curnode.lookup:
            return []
        else:
            dfs(curnode.lookup[char], char, res)
            # print(res)
            return res



