#--coding:utf-8--


# 可以抽象成二叉树去遍历，选取符合要求的路径

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.dfs(0, 0, n, "", res)
        return res

    def dfs(self, use_lt, use_rt, n, t_str, res):
        # if use_lt==n and use_rt==n:
        if len(t_str) == 2*n:
            res.append(t_str)
            return
        if use_lt<use_rt:
            return
        if use_lt<n:
            self.dfs(use_lt+1, use_rt, n, t_str+"(", res)
        if use_rt<n:
            self.dfs(use_lt, use_rt+1, n, t_str+")", res)


class Node:
    def __init__(self, s, use_lt, use_rt):
        self.s = s
        self.lt = use_lt # 已使用的左括号个数
        self.rt = use_rt # 已使用的右括号个数

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        if n==0: return res
        q = collections.deque()
        q.append(Node("", 0, 0))
        while q:
            cur_node = q.popleft()
            if cur_node.lt==n and cur_node.rt==n:
                res.append(cur_node.s)
            if cur_node.lt<n:
                q.append(Node(cur_node.s+"(", cur_node.lt+1, cur_node.rt))
            if cur_node.rt<n and cur_node.lt>cur_node.rt:
                q.append(Node(cur_node.s+")", cur_node.lt, cur_node.rt+1))
        return res
