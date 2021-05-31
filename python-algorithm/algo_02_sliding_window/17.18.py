#--coding:utf-8--
class Solution:
    def shortestSeq(self, big: List[int], small: List[int]) -> List[int]:
        record_dic = dict()
        for item in small:
            if item not in record_dic:
                record_dic[item] = 1
            else:
                record_dic[item] += 1
        i,j,cnt,res = 0,0,0,[]
        min_len = len(big)+1
        while j<len(big):
            if big[j] in record_dic:
                record_dic[big[j]] -= 1
                if record_dic[big[j]]>=0:
                    cnt += 1
            while cnt>=len(small):
                if j-i+1<min_len:
                    min_len = j-i+1
                    res = [i,j]
                tmp = big[i]
                if tmp in record_dic:
                    record_dic[tmp] += 1
                    if record_dic[tmp] >= 1:
                        cnt -= 1
                i += 1
            j += 1
        return res






