#--coding:utf-8--
'''
@Time   : 2019/8/24
@Author : Heng Li
@Email  : liheng_lulia@163.com
'''

# 对于此类问题，要搞明白每层循环的候选对象到底是什么！！！

class Solution:
    def restoreIpAddresses(self, s: str):
        res = []
        if len(s)<4:
            return res
        self.dfs(s, 0, 0, [], res)
        return res

    # 解决ip某一位分成01 010 之类的情况
    def condition(self, t_s):
        if len(t_s)>1 and t_s[0]=='0':
            return False
        return True

    def dfs(self, s, cnt, idx, cur_ls, res):
        if cnt==4:
            if idx==len(s):
                res.append(".".join(cur_ls))
            return
        for j in range(3):
            if idx+j<len(s) and int(s[idx:idx+j+1])<=255 and self.condition(s[idx:idx+j+1]):
                cur_ls.append(s[idx:idx+j+1])
                self.dfs(s, cnt+1, idx+j+1, cur_ls, res)
                cur_ls.pop()



if __name__ == "__main__":
    str1 = "1111"
    ip = Solution().restoreIpAddresses(str1)
    print(ip)