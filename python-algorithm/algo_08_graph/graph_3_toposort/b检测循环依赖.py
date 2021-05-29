# -*- coding: utf-8 -*-

'''
（1）循环依赖检测。如，[['A', 'B'], ['B', 'C'], ['C', 'D'], ['B', 'D']] => false，
[['A', 'B'], ['B', 'C'], ['C', 'A']] => true（2021.4 字节跳动-幸福里-后端）[2]

（2）手撕代码：小王写了一个makefile，其中有n个编译项编号为0~n-1，他们互相之间有依赖关系。
请写一个程序解析依赖，给出一个可行的编译顺序。（2021.03 字节跳动-系统部-后端

有的面试官要求判断是否有循环依赖；有的则要求给出一个可行的顺序。
解决这类问题的利器就是——拓扑排序

'''

'''
拓扑排序算法过程：
1. 选择图中一个入度为0的点，记录下来
2. 在图中删除该点和所有以它为起点的边
3. 重复1和2，直到图为空或没有入度为0的点。
'''
# 借助BFS来实现拓扑排序，队列中存储入度为0的点
# 同类题目：leetcode 课程表2

def haveCircularDependency(self, n: int, prerequisites):
    g = [[]for i in range(n)] #邻接表存储图结构
    indeg = [0 for i in range(n)] #每个点的入度
    res = [] #存储结果序列
    q = deque()
    #将依赖关系加入邻接表中g，并各个点入度
    for pre in prerequisites:
        a, b = pre[0], pre[1]
        g[a].append(b)
        indeg[b] += 1
    #一次性将入度为0的点全部入队
    for i in range(n):
        if indeg[i] == 0:
            q.append(i)
    while q:
        t = q.popleft()
        res.append(t)
        #删除边时，将终点的入度-1。若入度为0，果断入队
        for j in g[t]:
            indeg[j] -= 1
            if indeg[j] == 0:
                q.append(j)
    if len(res) == n:
        return res
    else:
        return []