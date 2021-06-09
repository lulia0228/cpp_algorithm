#
# @param s string字符串
# @return string字符串一维数组
#

class Solution:
    def restoreIpAddresses(self, s):
        # write code here
        res = []
        self.dfs(s, 0, 0, [], res)
        return res

    def dfs(self, s, cnt, idx, tmp_ls, res):
        if cnt == 4:
            if idx == len(s):
                ts = '.'.join(tmp_ls[:])
                res.append(ts)
            return
        for j in range(1, 4):
            if idx < len(s) and s[idx] == '0' and j > 1:
                continue
            if idx + j <= len(s) and int(s[idx:idx + j]) <= 255:
                tmp_ls.append(s[idx:idx + j])
                self.dfs(s, cnt + 1, idx + j, tmp_ls, res)
                tmp_ls.pop()

class Solution1:
    def restoreIpAddresses(self , s ):
        # write code here
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
        for j in range(1,4):
            if idx+j<=len(s) and int(s[idx:idx+j])<=255 and self.condition(s[idx:idx+j]):
                cur_ls.append(s[idx:idx+j])
                self.dfs(s, cnt+1, idx+j, cur_ls, res)
                cur_ls.pop()