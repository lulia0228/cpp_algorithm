#--coding:utf-8--

# 方法1 栈
# 把有效的叶子节点使用 "#" 代替。 比如把 4## 替换成 # 。此时，叶子节点会变成空节点！
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stack = list()
        for i in preorder.split(','):
            stack.append(i)
            while len(stack) > 2 and stack[-1] == '#' and stack[-2] == '#' and stack[-3].isdigit():
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append('#')
        return True if stack == ['#'] else False


# 方法2
# 性质：在树（甚至图）中，所有节点的入度之和等于出度之和
# 对每个节点而言，如果非空其入度为1 出度为2 ； 空节点入度为1 出度为0

class Solution(object):
    def isValidSerialization(self, preorder):
        nodes = preorder.split(',')
        # diff 表示的是出度-入度；
        # 初始化为1 是因为遍历第一个节点根节点的时候，没有入度，
        # 为了跟下面的每个节点入度-1操作抵消掉
        diff = 1
        for node in nodes:
            diff -= 1 # 入度-1
            # 遍历到当前节点，还没到其子节点时候，先不管出度
            # 还没遍历到该节点的子节点，此时遍历到的所有的出度应该大于等于入度

            if diff < 0:
                return False
            # 开始考虑出度
            if node != '#':
                diff += 2
        return diff == 0

