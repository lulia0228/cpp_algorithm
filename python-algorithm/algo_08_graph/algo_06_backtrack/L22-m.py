#--coding:utf-8--


# 可以抽象成二叉树去遍历，选取符合要求的路径

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        if n == 0:
            return res
        self.dfs("", 0, 0, n, res)
        return res

    def dfs(self, tmp_s, use_lt, use_rt, count, res):
        '''
        :param tmp_s:
        :param use_lt: 已经使用的左括号个数
        :param use_rt: 已经使用的右括号个数
        :param count:
        :param res:
        :return:
        '''
        if use_lt == count and use_rt == count:
            res.append(tmp_s)
            return
        if use_lt < use_rt:
            return
        if use_lt < count:
            self.dfs(tmp_s + "(", use_lt + 1, use_rt, count, res)
        if use_rt < count:
            self.dfs(tmp_s + ")", use_lt, use_rt + 1, count, res)



class Node:
    def __init__(self, s, lt, rt):
        self.s = s
        self.lt = lt # 剩余可使用的左括号个数
        self.rt = rt # 剩余可使用的右括号个数

class Solution1:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        if n==0:
            return res
        que = []
        que.append(Node("", n, n))
        while que != []:
            cur_node = que.pop(0) # 换成que.pop(-1)或者que.pop()相当于是模拟栈的功能
            if cur_node.lt==0 and cur_node.rt==0:
                res.append(cur_node.s)
            if cur_node.lt>0:
                que.append(Node(cur_node.s+"(", cur_node.lt-1, cur_node.rt))
            if cur_node.rt>0 and cur_node.lt<cur_node.rt:
                que.append(Node(cur_node.s+")", cur_node.lt, cur_node.rt-1))
        return res
