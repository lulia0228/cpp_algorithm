# -*- coding: utf-8 -*-
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        r_dic = {}
        for w in strs:
            t_k = "".join(sorted(list(w)))
            if t_k not in r_dic:
                r_dic[t_k] = [w]
            else:
                r_dic[t_k].append(w)
        res = [v for k, v in r_dic.items()]
        return res

