#--coding:utf-8--
'''
@Time   : 2020/8/14
@Author : Heng Li
@Email  : liheng_lulia@163.com
'''

# 另一种办法是各自遍历一次得到两者长度差值，然后快慢指针相遇
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node1, node2 = headA, headB
        while node1 != node2 :
            node1 = headB if node1 == None else node1.next
            node2 = headA if node2 == None else node2.next
        return node1