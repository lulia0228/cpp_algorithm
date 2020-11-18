#--coding:utf-8--

# 剑指 Offer 52. 两个链表的第一个公共节点

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        A, B = headA, headB
        while A != B:
            if A == None:
                A = headB
            else:
                A = A.next
            if B == None:
                B = headA
            else:
                B = B.next
        return A