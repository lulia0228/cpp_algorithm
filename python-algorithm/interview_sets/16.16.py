#--coding:utf-8--


class Solution:
    def subSort(self, array: List[int]) -> List[int]:
        new_ls = []
        for idx,item in enumerate(array):
            new_ls.append([item, idx])
        new_ls.sort()
        res = [-1, -1]
        # flag = False
        # for i in range(len(array)):
        #     if new_ls[i][1] != i:
        #         if not flag:
        #             res[0] = i
        #         flag = True
        #         res[1] = i
        i,j = 0, len(array)-1
        while i<len(array):
            if new_ls[i][1] != i:
                res[0] = i
                break
            i += 1
        while j>=0:
            if new_ls[j][1] != j:
                res[1] = j
                break
            j-= 1
        return res

