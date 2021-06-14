# -*- coding: utf-8 -*-

# class Interval:
#     def __init__(self, a=0, b=0):
#         self.start = a
#         self.end = b

#
# 树的直径
# @param n int整型 树的节点个数
# @param Tree_edge Interval类一维数组 树的边
# @param Edge_value int整型一维数组 边的权值
# @return int整型
#

class Solution:
    def __init__(self):
        self.max_distance = float('-inf')

    def solve(self, n, Tree_edge, Edge_value):
        # write code here
        from collections import defaultdict
        tree = defaultdict(list)
        for edge, weight in zip(Tree_edge, Edge_value):
            tree[edge.start].append((edge.end, weight))
            tree[edge.end].append((edge.start, weight))
        self.dfs(tree, 0, defaultdict(bool))
        return self.max_distance

    # 相当于是，带权值的无环图中，找一条路径使路径权重和最大
    def dfs(self, tree, position, visit):
        # 记录每个点连通的最大2个路径（因为是多叉树）
        top1_path, top2_path = 0, 0
        visit[position] = True
        # 理解成多叉树前序遍历dfs
        for child, weight in tree[position]:
            # 无环图。只需要保证不走回头路就可以了
            if visit[child]:
                continue
            weight += self.dfs(tree, child, visit)
            if weight > top1_path:
                top2_path = top1_path
                top1_path = weight
            elif weight > top2_path:
                top2_path = weight
            self.max_distance = max(top1_path + top2_path, self.max_distance)
        return max(top1_path, top2_path)
