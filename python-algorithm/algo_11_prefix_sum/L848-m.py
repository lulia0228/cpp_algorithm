#--coding:utf-8--

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        pos = [0]*len(shifts)
        pos[-1] = shifts[-1]
        for i in range(len(shifts)-2, -1, -1):
            pos[i] = pos[i+1]+shifts[i]
        res = ""
        for i in range(len(s)):
            res += chr( (ord(s[i])-97 + pos[i])%26 + 97)
        return res
