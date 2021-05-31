#--coding:utf-8--
# class Solution:
#     def findClosest(self, words: List[str], word1: str, word2: str) -> int:
#         p1 = p2 = -1
#         res =  float('inf')
#         for i in range(len(words)):
#             if word1 == words[i]:
#                 p1 = i
#             elif word2 == words[i]:
#                 p2 = i
#             if p1!=-1 and p2!=-1:
#                 res = min(res, abs(p1-p2))
#         return res

class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        record = dict()
        for i in range(len(words)):
            if words[i] not in record:
                record[words[i]] = [i]
            else:
                record[words[i]].append(i)
        i,j = 0,0
        res =  float('inf')
        while i<len(record[word1]) and j < len(record[word2]):
            res = min(res, abs(record[word1][i]-record[word2][j]))
            if record[word1][i] < record[word2][j]:
                i += 1
            else:
                j += 1
        return res