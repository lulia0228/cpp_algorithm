# -*- coding: utf-8 -*-
# 克鲁斯卡尔算法(Kruskal算法)求最小生成树

from queue import PriorityQueue
class Solution:
    def miniSpanningTree(self, n, m, cost: list):
        # n个点，m条边，每条边用cost列表存
        cost.sort(key=lambda c: c[2])
        point = [i for i in range(n)]
        tree = []
        ans = 0
        for fromw, tow, weight in cost:
            if point[fromw - 1] != point[tow - 1]:
                tree.append(cost)
                ans += weight
                if len(tree) == n - 1:
                # 最小生成树由n个点，n-1条边组成
                    break
                pfrom, pto = point[fromw - 1], point[tow - 1]
                for i in range(n):
                    if point[i] == pfrom:
                        point[i] = pto
        return ans