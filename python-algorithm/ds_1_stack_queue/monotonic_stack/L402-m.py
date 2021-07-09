#--coding:utf-8--

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stk = []
        cnt = 0
        leave = len(num)-k
        for c in num:
            while cnt<k and stk and int(stk[-1])>int(c):
                stk.pop()
                cnt += 1
            stk.append(c)
        # 此时stk中字符表达的数字一定是递增的
        # stk长度可能大于leave，因为可能出栈的字符个数不够k
        attend = "".join(stk[:leave]).lstrip("0")
        return  attend if attend != ""  else "0"

