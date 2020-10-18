#--coding:utf-8--


# 思路：
# 如果节点属于第一个集合，将其着为蓝色，否则着为红色。只有在二分图的情况下，
# 可以使用贪心思想给图着色：一个节点为蓝色，说明它的所有邻接点为红色，它的邻接点的所有邻接点为蓝色，依此类推。

# DFS 递归 系统栈
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        m = len(graph)
        # 标记节点颜色
        color = [-1 for i in range(m)]
        # 以每个未被访问的节点作为根节点，做深度遍历多叉树，每层遍历对象为上一层接单的邻接节点
        for i in range(m):
            if color[i] == -1 and not self.IsErFen(graph, i, 0, color):
                return False
        return True

    def IsErFen(self, graph, curNode, goalColor, color):
        if color[curNode] != -1:
            return color[curNode] == goalColor
        color[curNode] = goalColor
        # 遍历对象为curNode的邻接节点
        for adj_node in graph[curNode]:
            if not self.IsErFen(graph, adj_node, 1-goalColor, color):
                return False
        return True

# DFS 显式栈   在力扣上速度更快
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        m = len(graph)
        # 标记颜色
        color = [-1 for i in range(m)]
        for start in range(m):
            if color[start] == -1:
                stack = []
                stack.append(start)
                color[start] = 0
                while len(stack):
                    curNode = stack.pop(-1)
                    for nextNode in graph[curNode]:
                        if color[nextNode] == -1:
                            stack.append(nextNode)
                            color[nextNode] = 1-color[curNode]
                        else:
                            if color[nextNode] == color[curNode]:
                                return False
        return True

