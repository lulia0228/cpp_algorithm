#--coding:utf-8--
#
#
# @param s string字符串
# @return bool布尔型
#


class Solution:
    def isValid(self, s):
        # write code here
        stk = []
        for c in s:
            #  if c not in [')',']', '}']:
            if c != ')' and c != ']' and c != '}':
                stk.append(c)
            else:
                if stk:
                    tmp = stk.pop(-1)
                    if c == ')':
                        if tmp != '(': return False
                    elif c == ']':
                        if tmp != '[': return False
                    elif c == '}':
                        if tmp != '{': return False
                else:
                    return False
        return stk == []


