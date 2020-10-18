#--coding:utf-8--

class Solution:
    def reverseVowels(self, s: str) -> str:
        s_l = [c for c in s] # 字符串不可变，转成列表表达
        tt = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        lt, rt = 0, len(s)-1
        while lt < rt:
            while lt < rt and s_l[lt] not in tt:
                lt += 1
            while lt < rt and s_l[rt] not in tt:
                rt -= 1
            s_l[lt], s_l[rt] = s_l[rt], s_l[lt]
            lt += 1
            rt -= 1
        return ''.join(s_l)