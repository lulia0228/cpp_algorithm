#--coding:utf-8--
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        record = dict()
        for s in strs:
            tmp = "".join(sorted(list(s)))
            if tmp not in record:
                record[tmp] = [s]
            else:
                record[tmp].append(s)
        res = []
        for k,v in record.items():
            res.append(v)
        return res


