#--coding:utf-8--
class Solution:
    def removeDuplicates(self, S: str) -> str:
        if len(S)<2: return S
        stk = [S[0]]
        i = 1
        while i<len(S):
            if stk != [] and S[i] == stk[-1]:
                stk.pop(-1)
            else:
                stk.append(S[i])
            i += 1
        # res = ""
        # while stk: # 模拟栈
        #     res = stk.pop(-1)+res
        # return res
        return "".join(stk)