#--coding:utf-8--
# 栈排序
# @param a int整型一维数组 描述入栈顺序
# @return int整型一维数组
#
class Solution:
    def solve(self , a ):
        # write code here
        s = [] #定义一个栈用来存储数据(我们用数组来模拟)
        n  = len(a)
        res = []#用来返回结果
        vis = [0] *(n+1)#用来标记哪个数字出现过
        for i in a:
            s.append(i)#压入栈
            vis[i] = 1#压入一个数就把对应的数字标记为1
            while n and vis[n]: n -= 1#检测现有栈中有多少个数出现了就是较大的哪些数出现了（从大到小）
            while s and n <= s[-1]:
                #然后将栈中>=n的元素出栈
                res.append(s.pop(-1))
        #如果栈没为空就按照栈中原样直接出栈
        while s:
            res.append(s.pop(-1))
        return res