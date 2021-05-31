#--coding:utf-8--
# 算是回溯的思想
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[str]:
        total = []
        visited = [False] * (len(wordList))
        self.dfs(beginWord, endWord, wordList, [beginWord], total, visited)
        if total != []:
            return total[0]
        return total

    def dfs(self, begin, end, wordList, tmp, res, visited):
        if begin == end:
            res.append(tmp[:])
            return
        for i in range(len(wordList)):
            if not visited[i] and self.CanTrans(begin, wordList[i]):
                visited[i] = True
                tmp.append(wordList[i])
                self.dfs(wordList[i], end, wordList, tmp, res, visited)
                tmp.pop()
                # visited[i] = False # 关掉visited起了剪枝作用，不会超时

    def CanTrans(self, s1, s2):
        if len(s1) != len(s2): return False
        cnt = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                cnt += 1
                if cnt > 1: break
        return cnt == 1




