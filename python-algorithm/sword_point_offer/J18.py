# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        tmp_node = dummy
        while tmp_node.next.val != val:
            tmp_node = tmp_node.next
        tmp_node.next = tmp_node.next.next
        return dummy.next

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        tmp = dummy
        while head.val != val:
            tmp = head
            head = head.next
        tmp.next = head.next
        return dummy.next