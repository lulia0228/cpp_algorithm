#--coding:utf-8--

class Solution:
    def __init__(self, **kwargs):
        self.dt = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs",
        '8':"tuv", '9':"wxyz"}

    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if digits=="":
            return res
        self.findCombination(digits, 0, "", res)
        return res

    def findCombination(self, digits, index, tmp_s, res):
        if index == len(digits):
            res.append(tmp_s)
            return
        ch = digits[index]
        letters = self.dt[ch]
        for i in range(len(letters)):
            self.findCombination(digits, index+1, tmp_s+letters[i], res)

