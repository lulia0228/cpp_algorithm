# -*- coding: utf-8 -*-
# 节点(设为x)中序遍历的下一个节点有以下可能：
#
# （1）若x有右子树。则x的下一个节点为x右子树最左侧节点。如，2的下一个节点为8。
# （2）若x没有右子树，又分为2种情况。
# a. 若x是父节点的左孩子。则x的父节点就是x的下一个节点。如，7的下一个节点是4。
# b. 若x是父节点的右孩子。则沿着父节点向上，直到找到一个节点的父节点的左孩子是该节点，则该节点的父节点就是x的下一个节点。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.father = None # 指向父节点；如果一开始没这个指向，需要自行给每个节点增加此指向

class Solution():
    def getNext(self, pNode):
        if pNode.right:
            t_p = pNode.right
            while tp.left:
                tp = tp.left
            return t_p
        p = pNode
        while p.next:
            if p.father.left == p:
                return p.father
            p = p.father



