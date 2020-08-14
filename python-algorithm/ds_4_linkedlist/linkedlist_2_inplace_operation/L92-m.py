#--coding:utf-8--
'''
@Time   : 2020/8/14
@Author : Heng Li
@Email  : liheng_lulia@163.com
'''

# back cur front 分别表示上一个节点 当前节点 下一个节点

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy
        start = 0
        while start < m:
            point1 = cur # 记反转位置上一个节点
            cur = cur.next
            start += 1
        point2 = cur # 标记反转位置
        back = None
        while start <= n:
            front = cur.next
            cur.next = back
            back = cur
            cur = front
            start += 1
        point1.next = back
        point2.next = front
        return dummy.next