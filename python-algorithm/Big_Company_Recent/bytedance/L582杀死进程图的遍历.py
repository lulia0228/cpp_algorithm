# -*- coding: utf-8 -*-

# 有点类似课程表问题

# DFS或者BFS
class Solution:
    def killProcess(self, pid_list, ppid_list, kill_no):
        r_dic = {}
        for i in range(len(pid_list)):
            if ppid_list[i]:
                if ppid_list[i] not in r_dic:
                    r_dic[ppid_list[i]] = [pid_list[i]]
                else:
                    r_dic[ppid_list[i]].append(pid_list[i])
        res = []
        self.dfs(kill_no, r_dic, res)
        return res

    def dfs(self, kill_no, r_d, res):
        if kill_no not in r_d:
            return
        res.append(kill_no)
        for i in r_d[kill_no]:
            self.dfs(i, r_d, res)

class Solution1:
    def killProcess(self, pid_list, ppid_list, kill_no):
        r_dic = {}
        for i in range(len(pid_list)):
            if ppid_list[i]: # 可以不要
                if ppid_list[i] not in r_dic:
                    r_dic[ppid_list[i]] = [pid_list[i]]
                else:
                    r_dic[ppid_list[i]].append(pid_list[i])
        res = []
        que = []
        que.append(kill_no)
        while que:
            front = que.pop(0)
            res.append(front)
            for i in r_dic[front]:
                que.append(i)
        return res
