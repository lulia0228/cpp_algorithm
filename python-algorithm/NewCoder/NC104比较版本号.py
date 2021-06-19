# -*- coding: utf-8 -*-
class Solution:
    def compare(self , version1 , version2 ):
        # write code here
        v1 = version1.split(".")
        v2 = version2.split(".")
        s1, s2 = len(v1), len(v2)
        if len(v1) < len(v2):
            v1.extend(["0"]*(s2-s1))
        elif len(v1) > len(v2):
            v2.extend(["0"]*(s1-s2))
        for i in range(len(v1)):
            if int(v1[i]) < int(v2[i]):
                return -1
            elif int(v1[i]) > int(v2[i]):
                return 1
        return 0

version1 , version2 = "1.0","1.0.0"
res = Solution().compare(version1, version2)
print(res)